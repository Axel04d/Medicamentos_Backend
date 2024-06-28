from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    enfermedad = models.TextField()

    def __str__(self):
        return self.nombre
