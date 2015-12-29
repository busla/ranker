from django.forms import inlineformset_factory, modelformset_factory, modelform_factory
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.db.models import Max, Min, Sum, Count, Prefetch
from django.views.decorators.cache import cache_page
from django.conf import settings
import collections

from .custom.ranking_points import RankingPoints

if settings.DEBUG:
    caching = cache_page(0)

else:
    caching = cache_page(60 * 10)

def home(request):    
    #athletes = Athlete.objects.all()
    cat = []
    categories = Category.objects.all()

    for category in categories:
        cat.append({'id': category.id, 'title': category.title})
    
    t = loader.get_template('app/ranking.html')
    c = RequestContext(request, {'index':'index', 'categories': cat})
    return HttpResponse(t.render(c))

@login_required(login_url='/admin/')
def add_results(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = ResultsForm(request.POST)        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form = ResultsForm(request.POST)
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        ResultsFormSet = modelformset_factory(Results, form=ResultsForm)
        form = ResultsFormSet(queryset=Results.objects.none())
        #form = modelformset_factory(Results, fields=("athlete", "tournament", "category"))
        #form = modelform_factory(Results, fields=("athlete", "tournament", "category"))

        #form = ResultsForm()

    return render(request, 'app/forms/add_results.html', {'form': form})

def calculate_points(result):
    total = 0
    points_list = []

    category_points = result.category_points()
    attribute_points = result.attribute_points()     

    points_list = category_points + attribute_points


    for item in points_list:
        for key in item:
            if 'points' in key:
                total += item['points']


    return total

#@cache_page(60 * 60 * 24)
@caching
def score(request):
    data = []
    cat = []
    profile = []
    athletes = Athlete.objects.filter(club__site=request.site)

    results = Results.objects \
        .select_related('athlete') \
        .select_related('category') \
        .select_related('tournament') \
        .prefetch_related('tournament__score_system') \
        .prefetch_related('tournament__score_system__category') \
        .prefetch_related('tournament__score_system__score')
    
    """
    This iteration is heavy and has to be cached.
    """

    for athlete in athletes:
        total = 0
        #for result in athlete.results_set.prefetch_related('tournament__score_system__score'):               
        for result in results.filter(athlete=athlete):

            total += calculate_points(result)
                    
        #data.append({'name': athlete.name, 'id': athlete.id, 'points': total, 'categories': categories})
        data.append({'name': athlete.name, 'id': athlete.id, 'points': total})



     
    #return render_to_response('app/ranking.html', {data})
    return JsonResponse(data, safe=False)

@caching
def category(request, cat=None):
    data = []
    
    athletes = Athlete.objects.filter(club__site=request.site)

    for athlete in athletes:
        total = 0
        for result in athlete.results_set.filter(category=int(cat)).prefetch_related('tournament__score_system'):               
            total += calculate_points(result)            

        data.append({'name': athlete.name, 'id': athlete.id, 'points': total})


    return JsonResponse(data, safe=False)
   

def athlete(request, pk=None):   
    data = []
    record = []    

    athlete = Athlete.objects.get(pk=int(pk))
    
    for result in athlete.results_set.all().order_by('tournament__date', '-category'):      
        total = 0
        points =  {}
        points_list = []        

        category_points = result.category_points()
        attribute_points = result.attribute_points()     

        points_list = category_points + attribute_points
        

        for item in points_list:
            for key in item:
                if 'points' in key:
                    total += item['points']
        
        points.update({
            'name': result.athlete.name,                             
            'event': result.tournament.title,
            'category': result.category.title,
            'date': result.tournament.date,
            'points': points_list,            
            'total': total,            
        })

        
        record.append(points)


    data.append({'records': record})                    
    

    return JsonResponse(data, safe=False)

#@caching
def score_system(request):
    data = []
    qs = ScoreSystem.objects.select_related('category').prefetch_related('score').order_by('title')

    for item in qs:
        for score in item.score.all().order_by('place'):
            data.append({   
                'title': item.title,                             
                'score': score.title,
                'scale': item.scale,
                'category': item.category,            
                'place': score.place,
                'points': score.value,
                'total': score.value * item.scale,
                })        
    

    t = loader.get_template('app/score_system.html')
    c = RequestContext(request, {'data': data})
    return HttpResponse(t.render(c))

