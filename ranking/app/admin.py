from django.contrib import admin
from .models import *

class ResultsAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'tournament', 'category', 'score')    
    list_editable = ['tournament']
    search_fields = ['athlete__name']

admin.site.register(Athlete)
admin.site.register(Tournament)
admin.site.register(Category)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Image)
admin.site.register(ScoreSystem)
admin.site.register(ScoreItem)
