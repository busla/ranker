from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render_to_response
from .models import *
from django.db.models import Max, Min, Sum, Count, Prefetch
from django.views.decorators.cache import cache_page

def home(request):    
    #athletes = Athlete.objects.all()

    return render_to_response('app/ranking.html', {'index':'index'})

@cache_page(60 * 60 * 24)
def score(request):
    data = []
    profile = []
    athletes = Athlete.objects.all()

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
            for score in result.tournament.score_system.filter(category=result.category):
                if result.category == score.category:
                    for point in score.score.all():                        
                        if result.score == point.place or 'other' in point.tags.names():                    
                                total += point.points * score.scale
                        
        
        data.append({'name': athlete.name, 'id': athlete.id, 'points': total})



     
    #return render_to_response('app/ranking.html', {data})
    return JsonResponse(data, safe=False)

@cache_page(60 * 60 * 24)
def category(request, cat=None):
    data = []
    
    athletes = Athlete.objects.all()

    for athlete in athletes:
        total = 0
        for result in athlete.results_set.filter(category=int(cat)).prefetch_related('tournament__score_system'):               
            for score in result.tournament.score_system.filter(category=result.category):
                if result.category == score.category:
                    for point in score.score.all():                        
                        if result.score == point.place or 'other' in point.tags.names():                    
                            total += point.points * score.scale
        
        data.append({'name': athlete.name, 'id': athlete.id, 'points': total})


    return JsonResponse(data, safe=False)

def athlete(request, pk=None):
    data = []
    record = []                                   
    athlete = Athlete.objects.get(pk=int(pk))

    for result in athlete.results_set.all().order_by('tournament__date', '-category'):
        for score in result.tournament.score_system.filter(category=result.category):
            if result.category == score.category:                
                for point in score.score.all():                        
                    if result.score == point.place or 'other' in point.tags.names():                    
                        record.append({   
                            'name': result.athlete.name,                             
                            'tournament': result.tournament.title,
                            'category': result.category.title,
                            'date': result.tournament.date,
                            'place': result.score,
                            'points': point.points * score.scale,
                            })                         

    data.append({'record': record})                    


    return JsonResponse(data, safe=False)

@cache_page(60 * 60 * 24)
def score_system(request):
    data = []
    qs = ScoreSystem.objects.select_related('category').prefetch_related('score')

    for item in qs:
        for score in item.score.all():
            data.append({   
                'title': item.title,                             
                'score': score.title_rendered,
                'scale': item.scale,
                'category': item.category,            
                'place': score.place,
                'points': score.points,
                'total': score.points * item.scale,
                })        
    


    return render_to_response('app/score_system.html', {'data': data})

