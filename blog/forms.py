from django import forms
from django.forms.models import ModelForm

from .models import Publicacion 

class PublicacionForm(forms,ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'texto',)