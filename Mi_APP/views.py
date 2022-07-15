from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from Mi_APP.models import Candidatos, Reclutadores, Sectores
from Mi_APP.forms import formReclutadores, formCandidatos

def index(request):
    return render (request, "Mi_APP/index.html", {})

def form_Reclutadores(request):
    if request.method == 'POST':
        formReclu = formReclutadores(request.POST)

        if formReclu.is_valid():
            datos = formReclu.cleaned_data
            reclutador = Reclutadores (nombre = datos["nombre"], apellido = datos["apellido"], DNI = datos["DNI"])
            reclutador.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
        return render (request, "Mi_APP/index.html") #vuelve al inicio
        
    else:
        formReclu = formReclutadores()
        return render (request, "Mi_APP/reclutadores.html",{"formReclu":formReclu})


def form_Candidatos(request):
    if request.method == 'POST':
        formCand = formCandidatos(request.POST)

        if formCand.is_valid():
            datos = formCand.cleaned_data
            reclutador = Candidatos (nombre = datos["nombre"], apellido = datos["apellido"], DNI = datos["DNI"])
            reclutador.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
        return render (request, "Mi_APP/index.html") #vuelve al inicio
        
    else:
        formCand = formCandidatos()
        return render (request, "Mi_APP/candidatos.html",{"formCand":formCand})


def listar_reclutadores(request):
    context = {}
    context["reclutadores"] = Reclutadores.objects.all() #modelo #diccionario
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
