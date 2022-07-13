from django.shortcuts import render
from Mi_APP.models import Reclutadores

def listar_reclutadores(request):
    context = {}
    context["reclutadores"] = Reclutadores.objects.all()
    return render (request, 'Mi_APP/listar_reclutadores.html', context)

def mostrar_Mensajes(request):
    return render(request, 'Mi_APP/Mensajes.html', {})

def mostrar_Otros(request):
    return render(request, 'Mi_APP/Otros.html', {})

def mostrar_Perfil(request):
    return render(request, 'Mi_APP/Perfil.html', {})

# Create your views here.
