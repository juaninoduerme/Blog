from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.inicio),
    path('Inicio', views.inicio),
    path('Peliculas', views.peliculas),
    path('Series', views.series),
    path('Generos', views.generos),
]