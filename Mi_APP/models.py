from django.db import models

class Reclutadores(models.Model):
    nombre_r = models.CharField(max_length=40)
    apellido_r = models.CharField(max_length=40)
    DNI_r = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_r} {self.apellido_r} {self.DNI_r}"

class Candidatos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    DNI = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.DNI}"

class Sectores(models.Model):
    nombre_sector = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)
    modalidad = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre_sector} {self.turno} {self.modalidad}"

# Create your models here.
