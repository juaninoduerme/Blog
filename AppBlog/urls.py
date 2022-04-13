from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Peliculas', views.peliculas, name="Peliculas"),
    path('Peliculas Formulario', views.peliculasFormulario, name="PeliculasFormulario"),
    path('Series', views.series, name="Series"),
    path('Series Formulario', views.seriesFormulario, name="SeriesFormulario"),
    path('Videos', views.videos, name="Videos"),
    path('Videos Formulario', views.videosFormulario, name="VideosFormulario"),
    path('Busqueda de Películas', views.busqueda, name="BusquedaPelicula"),
    path('Buscar', views.buscar),
]