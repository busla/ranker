from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.helpers import ActionForm
from .forms import *
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *


class ResultsInline(admin.TabularInline):
    model = Results

class AttributeInline(admin.TabularInline):
    model = Attribute


class AttributeAdmin(admin.ModelAdmin):
    pass

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'rank_system')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')    
    readonly_fields = ('slug',)

class ClubAdmin(admin.ModelAdmin):
    list_display = ['title']

class ScoreItemAdmin(admin.ModelAdmin):
    list_display = ('title_rendered', 'place', 'value', 'slug', 'attribute_item')    
    readonly_fields = ('slug',)


class ScoreSystemAdmin(admin.ModelAdmin):
    list_display = ('title', 'scale', 'category')    


class AttributeItemAdmin(admin.ModelAdmin):
    pass

class ResultsAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'tournament', 'category')    
    search_fields = ['athlete__name']
    
    inlines = [
        AttributeInline
    ]

    def get_queryset(self, request):
        qs = super(ResultsAdmin, self).get_queryset(request)
        profile = UserProfile.objects.get(user=request.user.id) 
        clubs = profile.club.all()
        return qs.filter(athlete_club__in=clubs)

class AthleteAdmin(admin.ModelAdmin):
    list_display = ('name', 'ssn', 'club')    
    search_fields = ['name']
    action_form = RegisterParticipationForm
    actions = ['register_participation']

    inlines = [
        ResultsInline
    ]

    def get_queryset(self, request):
        qs = super(AthleteAdmin, self).get_queryset(request)
        profile = UserProfile.objects.get(user=request.user.id) 
        clubs = profile.club.all()
        return qs.filter(club__in=clubs)
    
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

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login')  
    inlines = (UserProfileInline, )
"""

    def user_club(self, object):
        return object.person.name

    #user_club.short_description = 'Clubs'

    def queryset(self, request):
        # Prefetch related objects
        return super(UserAdmin, self).queryset(request).select_related('person')
"""
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Image)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeItem, AttributeItemAdmin)
admin.site.register(ScoreSystem, ScoreSystemAdmin)
admin.site.register(ScoreItem, ScoreItemAdmin)
