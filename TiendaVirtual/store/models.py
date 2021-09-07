from django.db import models

# Create your models here.

class user(models.Model):
    nombre = models.CharField(max_length=30)
    Correo = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    class Meta:
        db_table = "store_user"