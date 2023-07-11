from django import forms
from djangoModels_josh.model import Register

class Majina(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"