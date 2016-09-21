from django.shortcuts import render
from .models import *


def lista(request):
    nomi = Persona.objects.all() #estraggo dal db
    return render(request, 'rubrica/lista.html', {'nomi': nomi})
