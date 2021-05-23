  
from django.core import validators
from django import forms
from .models import Population

class PopulationRegistration(forms.ModelForm):
    class Meta:
        model = Population
        fields = '__all__'