from django import forms
from Actor.models import Actor  

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'