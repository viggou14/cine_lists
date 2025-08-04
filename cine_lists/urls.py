"""
URL configuration for cine_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/movies/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('movies', views.movies, name='movies'),
    path('movie/<int:movie_id>', views.movie, name='movie'),
    path('new_movie', views.new_movie, name='new_movie'),
    path('success', views.success, name='success'),
    path('new_entry/<movie_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),
    path('remove_entry/<entry_id>', views.remove_entry, name='remove_entry'),
    path('remove_movie/<int:movie_id>', views.remove_movie, name='remove_movie'),
]
