from django.db import models
from django_mysql.models import JSONField

# Create your models here.
from django.utils import timezone


class Inventario(models.Model):
    serie = models.CharField(max_length=200)
    cantidad = models.FloatField()
    precio =  models.FloatField()
    created_date = models.DateTimeField(
            default=timezone.now)


class Carga(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='ficheros')
    my_json_field = JSONField(blank=True)
