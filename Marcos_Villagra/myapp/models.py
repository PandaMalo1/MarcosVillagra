from django.db import models

# Create your models here.

class autor(models.Model): 
    Nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.Nombre}{self.apellido}"

class Libro(models.Model):
    Titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()

class Editorial(models.model):
    nombre = models.CharField(max_length=200)
    libros = models.ManyToManyField(Libro)

    def _str_(self):
        return self.nombre
