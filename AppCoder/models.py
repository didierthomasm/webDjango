from django.db import models

# Create your models here.
class Medicina(models.Model):
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    caducidad = models.DateField()
    existencia = models.BooleanField()

    def __str__(self):
        return self.nombre + ' (' + str(self.camada) + ')'

class Comestible(models.Model):
    nombre = models.CharField(max_length=40)
    tamano = models.IntegerField()
    caducidad = models.DateField()
    existencia = models.BooleanField()

class Limpieza(models.Model):
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    tamano = models.IntegerField()
    existencia = models.BooleanField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

