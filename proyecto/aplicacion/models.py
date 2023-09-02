from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alquileres(models.Model):
    tipo= models.CharField(max_length=50)
    ambientes= models.IntegerField()
    localidad = models.CharField(max_length=50)
    precio= models.IntegerField()
     

    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"
         

class Venta(models.Model):
    tipo= models.CharField(max_length=30)
    ambientes= models.IntegerField()
    localidad = models.CharField(max_length=50)
    precio= models.IntegerField()
    
class Asesores(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    telefono= models.IntegerField()
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Asesor"
        verbose_name_plural = "Asesores"

class Inversiones(models.Model):
    etapa= models.CharField(max_length=20)
    ambientes= models.IntegerField()
    localidad = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    class Meta:
        verbose_name = "Inversion"
        verbose_name_plural = "Inversiones"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
