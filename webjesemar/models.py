from django.db import models
from django.utils import timezone

# Create your models here.

class Suscriptor(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50,verbose_name="la direccion")
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=11)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nombre