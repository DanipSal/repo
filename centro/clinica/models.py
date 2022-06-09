from django.db import models

# Create your models here.



class Pacientes(models.Model):

    nombre = models.CharField(max_length=40)
    DNI = models.IntegerField()
    nacimiento = models.DateField()

class Medico(models.Model):

    medico = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)

class Turnos(models.Model):
    
    fechaturno = models.DateField()
    especialidad = models.CharField(max_length=40)


     


    