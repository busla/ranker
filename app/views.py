from django.http import JsonResponse
from django.shortcuts import render_to_response
from .models import *
from django.db.models import Max, Min, Sum, Count


def home(request):
    
    #athletes = Athlete.objects.all()
    return render_to_response('app/base.html', {})

def score(request):
    data = []
    profile = []
    athletes = Athlete.objects.all()

    for athlete in athletes:
        total = 0
        #for result in athlete.results_set.prefetch_related('tournament__score_system__score'):               
        for result in athlete.results_set.all():               
            for score in result.tournament.score_system.filter(category=result.category):
                if result.category == score.category:
                    for point in score.score.all():                        
                        if result.score == point.place or 'other' in point.tags.names():                    
                                total += point.points * score.scale
                        
        
        data.append({'name': athlete.name, 'id': athlete.id, 'points': total})



     

    return JsonResponse(data, safe=False)


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