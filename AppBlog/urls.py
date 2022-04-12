from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Peliculas', views.peliculas, name="Peliculas"),
    path('Series', views.series, name="Series"),
    path('Generos', views.generos, name="Generos"),
    path('Busqueda', views.busqueda, name="Busqueda"),
]