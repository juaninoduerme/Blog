from django.http.request import QueryDict
from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import Pelicula, Serie, Video
from AppBlog.forms import PeliculaFormulario, SerieFormulario, VideoFormulario

def inicio(request):
    return render(request, "AppBlog/templateInicio.html")

def peliculas(request):
    return render(request, "AppBlog/templatePelicula.html")

def peliculasFormulario(request):
    
    if request.method == 'POST':
        miFormulario = PeliculaFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pelicula = Pelicula(nombreOriginal=informacion['nombreOriginal'], nombreTraduccion=informacion['nombreTraduccion'], fechaDeEstreno=informacion['fechaDeEstreno'], genero=informacion['genero'], director=informacion['director'], guionista=informacion['guionista'], sinopsis=informacion['sinopsis'])
            pelicula.save()
            return render(request, "AppBlog/templatePelicula.html")
    else:
        miFormulario = PeliculaFormulario()
        
    return render(request, "AppBlog/templatePeliculaForm.html", {"miFormulario":miFormulario})

def series(request):
    return render(request, "AppBlog/templateSerie.html")

def seriesFormulario(request):
    
    if request.method == 'POST':
        miFormulario = SerieFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            serie = Serie(nombreOriginal=informacion['nombreOriginal'], nombreTraduccion=informacion['nombreTraduccion'], fechaDeEstreno=informacion['fechaDeEstreno'], genero=informacion['genero'], guionista=informacion['guionista'], temporadasEmitidas=informacion['temporadasEmitidas'], sinopsis=informacion['sinopsis'])
            serie.save()
            return render(request, "AppBlog/templateSerie.html")
    else:
        miFormulario = SerieFormulario()
        
    return render(request, "AppBlog/templateSerieForm.html", {"miFormulario":miFormulario})

def videos(request):
    return render(request, "AppBlog/templateVideo.html")

def videosFormulario(request):
    if request.method == 'POST':
        miFormulario = VideoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            video = Video(nombreOriginal=informacion['nombreOriginal'], nombreTraduccion=informacion['nombreTraduccion'], fechaDeEstreno=informacion['fechaDeEstreno'], genero=informacion['genero'], creador=informacion['creador'], plataforma=informacion['plataforma'], sinopsis=informacion['sinopsis'])
            video.save()
            return render(request, "AppBlog/templateVideo.html")
    else:
        miFormulario = VideoFormulario()
        
    return render(request, "AppBlog/templateVideoForm.html", {"miFormulario":miFormulario})

def busqueda(request):
    return render(request, "AppBlog/templateBusquedaPelicula.html")

def buscar(request):
    if(request.GET["nombreOriginal"]):
        nombre = request.GET["nombreOriginal"]
        peliculas = Pelicula.objects.filter(nombreOriginal__icontains = nombre)
        return render(request, "AppBlog/templateResultadoBusquedaPelicula.html", {"peliculas": peliculas, "nombre": nombre})
    else:
        respuesta = "No enviaste datos :("
    
    return HttpResponse(respuesta)