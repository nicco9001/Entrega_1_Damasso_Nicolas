from django.db import models

class Reclutadores(models.Model):
    nombre_r = models.CharField(max_length=40)
    apellido_r = models.CharField(max_length=40)
    DNI_r = models.IntegerField()
    
class Candidatos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    DNI = models.IntegerField()

class Sectores(models.Model):
    nombre_sector = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)
    modalidad = models.CharField(max_length=40)

# Create your models here.
