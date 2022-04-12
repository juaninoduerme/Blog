from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Genero
from AppBlog.models import Pelicula
from AppBlog.models import Serie
from django.template import loader

def mostrar_peliculas(self):
        
    peliculas = dict
    #peliculas = 
    
    plantilla = loader.get_template('templatePelicula.html')
    documento = plantilla.render(peliculas)
        
    return HttpResponse(documento)

def mostrar_series(self):
        
    series = dict
    #series = 
    
    plantilla = loader.get_template('templateSerie.html')
    documento = plantilla.render(series)
        
    return HttpResponse(documento)

def mostrar_generos(self):
        
    generos = dict
    #generos = 
    
    plantilla = loader.get_template('templateGenero.html')
    documento = plantilla.render(generos)
        
    return HttpResponse(documento)
