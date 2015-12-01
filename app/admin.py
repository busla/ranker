from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.helpers import ActionForm
from .forms import *
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render

from .models import *

class ResultsInline(admin.TabularInline):
    model = Results

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'rank_system')

    inlines = [
        ResultsInline
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')    
    readonly_fields = ('slug',)

class ScoreItemAdmin(admin.ModelAdmin):
    list_display = ('title_rendered', 'place', 'points', 'slug')    
    readonly_fields = ('slug',)

class ScoreSystemAdmin(admin.ModelAdmin):
    list_display = ('title', 'scale', 'category')    


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'tournament', 'category', 'score')    
    search_fields = ['athlete__name']

    

class AthleteAdmin(admin.ModelAdmin):
    action_form = RegisterParticipationForm
    actions = ['register_participation']

    def register_participation(modeladmin, request, queryset):        

        tournament = Tournament.objects.get(pk=request.POST['tournament'])
        score_system = tournament.score_system.get(category__slug='participation')        
        place = score_system.score.all()[0].place

        for athlete in queryset:
            
            result = Results(
                tournament=tournament,
                score=place,
                category=score_system.category,
                athlete=athlete)
            result.save()

            

        modeladmin.message_user(request, ("Successfully registered %d athletes") % (queryset.count(),), messages.SUCCESS)
    register_participation.short_description = "Register participation in tournament"

admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Image)
admin.site.register(ScoreSystem, ScoreSystemAdmin)
admin.site.register(ScoreItem, ScoreItemAdmin)
