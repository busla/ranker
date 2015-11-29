from django.contrib.admin.helpers import ActionForm
from django import forms
from .models import Tournament


class RegisterParticipationForm(ActionForm):
    #_selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all())

