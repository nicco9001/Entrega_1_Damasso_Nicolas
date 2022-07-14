from django.shortcuts import render
from Mi_APP.models import Candidatos, Reclutadores, Sectores

def index(request):
    return render (request, "Mi_APP/index.html", {})

def listar_reclutadores(request):
    context = {}
    context["reclutadores"] = Reclutadores.objects.all()
    return render (request, 'Mi_APP/listar_reclutadores.html', context)

def listar_candidatos(request):
    context = {}
    context["lista_candidatos"] = Candidatos.objects.all()
    return render (request, 'Mi_APP/listar_candidatos.html', context)

def sectores (request):
    context = {}
    context["sectores"] = Sectores.objects.all()
    return render (request, 'Mi_APP/sectores.html', context)

# Create your views here.
