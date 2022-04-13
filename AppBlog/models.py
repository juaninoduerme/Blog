from django.db import models

#MODELOS DEL BLOG    
class Pelicula(models.Model):
    idPelicula = models.AutoField(primary_key=True)
    nombreOriginal = models.CharField(max_length=100)
    nombreTraduccion = models.CharField(max_length=100)
    fechaDeEstreno = models.DateField()
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    guionista = models.CharField(max_length=100)
    sinopsis = models.CharField(max_length=500)
    
class Serie(models.Model):
    idSerie = models.AutoField(primary_key=True)
    nombreOriginal = models.CharField(max_length=100)
    nombreTraduccion = models.CharField(max_length=100)
    fechaDeEstreno = models.DateField()
    genero = models.CharField(max_length=100)
    guionista = models.CharField(max_length=100)
    temporadasEmitidas = models.IntegerField()
    sinopsis = models.CharField(max_length=500)
    
class Video(models.Model):
    idVideo = models.AutoField(primary_key=True)
    nombreOriginal = models.CharField(max_length=100)
    nombreTraduccion = models.CharField(max_length=100)
    fechaDeEstreno = models.DateField()
    genero = models.CharField(max_length=100)
    creador = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=100)
    sinopsis = models.CharField(max_length=500)