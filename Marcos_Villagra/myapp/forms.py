from django import forms
from .models import Libro

class LibroBusquedaForm(forms.Form):
    titulo = forms.CharField(max_length=200,required=False)
    autor = forms.charfield(max_length=100, required=False)
    