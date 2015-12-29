from django.contrib.admin.helpers import ActionForm
from django import forms
from .models import *
import autocomplete_light

class RegisterParticipationForm(ActionForm):
    #_selected_action = forms.CharField(widget=forms.MultipleHiddenInput)

    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all())

class ResultsForm(forms.ModelForm):
    
    class Meta:
        model = Results
        fields = ['athlete', 'tournament', 'category']
