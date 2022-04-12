from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppBlog/templateInicio.html")

def peliculas(request):
    return render(request, "AppBlog/templatePelicula.html")

def series(request):
    return render(request, "AppBlog/templateSerie.html")

def generos(request):
    return render(request, "AppBlog/templateGenero.html")