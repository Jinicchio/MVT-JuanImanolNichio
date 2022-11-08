from django.shortcuts import render
from django.template import loader
from .models import Familiar
from django.http import HttpResponse
# Create your views here.


def familia_view(request):
    plantilla = loader.get_template('Familia.html')
    context = { 'familiares': Familiar.objects.all()}
    documento = plantilla.render(context)
    return HttpResponse(documento)