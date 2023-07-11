from django.shortcuts import render
from djangoModels_josh.form import Majina


def Home(request):
    jina = Majina()
    return render(request, 'index.html', {'form': jina})
