from django.db import models

# Create your models here.

class user(models.Model):
    nombre = models.CharField(max_length=30)
    Correo = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    class Meta:
        db_table = "store_user"

class product(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    precio = models.FloatField(blank=True)
    talla = models.CharField(max_length=3)		
    categoria = models.CharField(max_length=8, blank=True)
    descripción = models.TextField(max_length=500)
    stock = models.PositiveIntegerField(default=1)
    imagen = models.ImageField(upload_to='products/')

    class Meta:
        db_table = "store_product"