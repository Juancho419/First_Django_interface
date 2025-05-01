from django.db import models

class Persona(models.Model):
    nombre =models.CharField(max_length=100)
    meta = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nombre} - {self.meta}"
    

# Create your models here.
