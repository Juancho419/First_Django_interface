from django.shortcuts import render
from .models import Persona

def bienvenida(request):
    personas = Persona.objects.all()
    return render(request, 'bienvenida.html', {'personas': personas})
