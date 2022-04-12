"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppBlog.views import mostrar_peliculas
from AppBlog.views import mostrar_series
from AppBlog.views import mostrar_generos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('peliculas/', mostrar_peliculas),
    path('series/', mostrar_series),
    path('generos/', mostrar_generos),
]
