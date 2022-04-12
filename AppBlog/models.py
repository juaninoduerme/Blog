from django.db import models

#MODELOS DEL BLOG
class Genero(models.Model):
    idGenero = models.IntegerField(primary_key=True)
    nombreGenero = models.CharField(max_length=100)
    
class Pelicula(models.Model):
    idPelicula = models.IntegerField(primary_key=True)
    nombreOriginal = models.CharField(max_length=100)
    nombreTraduccion = models.CharField(max_length=100)
    fechaDeEstreno = models.DateField()
    genero = models.ForeignKey(Genero)
    director = models.CharField(max_length=100)
    guionista = models.CharField(max_length=100)
    
class Serie(models.Model):
    idSerie = models.IntegerField(primary_key=True)
    nombreOriginal = models.CharField(max_length=100)
    nombreTraduccion = models.CharField(max_length=100)
    fechaDeEstreno = models.DateField()
    genero = models.ForeignKey(Genero)
    guionista = models.CharField(max_length=100)
    temporadasEmitidas = models.DecimalField()