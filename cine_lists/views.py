from django.shortcuts import render
from .models import Movie, Entry
from .forms import MovieForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """Página inicial do Learning Log"""
    return render(request, 'cine_lists/index.html')

def movies (request):
    """Mostra todos os filmes criados"""
    movies = Movie.objects.filter(owner=request.user).order_by('date_added')
    context = {'movies': movies}

    return render(request, 'cine_lists/index.html', context)

def movie(request, movie_id):
    """Mostra o filme e seus registros"""
    movie = Movie.objects.get(id=movie_id)

    #Garante que a anotação seja visível apenas para o dono
    if movie.owner != request.user:
        raise Http404
    
    entries = movie.entry_set.order_by('-date_added')
    context = {'movie': movie, 'entries': entries}
    return render(request, 'cine_lists/movie.html', context)


def new_movie(request):
    """Adiciona um novo filme"""
    if request.method != 'POST':
        #Nada foi enviado, retorna um formulario em branco
        form = MovieForm()
    else:
        #Dados do método POST enviados, processa os dados
        form = MovieForm(request.POST)
        if form.is_valid():
            new_movie = form.save(commit=False)
            new_movie.owner =request.user
            new_movie.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'cine_lists/new_movie.html', context)
