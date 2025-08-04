from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry, Movie
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
    movies = Movie.objects.all().order_by('date_added')
    context = {'movies': movies}

    return render(request, 'cine_lists/movies.html', context)

def movie(request, movie_id):
    """Mostra o filme e seus registros"""
    movie = Movie.objects.get(id=movie_id)
    
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
            form.save()
            return HttpResponseRedirect(reverse('success'))
    context = {'form': form}
    return render(request, 'cine_lists/new_movie.html', context)

def success(request):
    """Página de confirmação de envio"""
    movie = Movie.objects.last()

    context = {'movie': movie}
    return render(request, 'cine_lists/success.html', context)

def new_entry(request, movie_id):
    """Adciona uma nova anotação ao Filme atual"""
    movie = Movie.objects.get(id=movie_id)

    if request.method != 'POST':
        #Nenhum dado enviado. Cria formulário em branco
        form =EntryForm()
    else:
        #Dados em método POST enviados
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.movie = movie
            new_entry.save()
            return HttpResponseRedirect(reverse('movie', args=[movie_id]))
    context = {'movie': movie, 'form': form}
    return render(request, 'cine_lists/new_entry.html', context)

def edit_entry(request, entry_id):
    """"Edita uma anotação existente"""
    entry = Entry.objects.get(id=entry_id)
    movie = entry.movie

    if request.method != 'POST':
        #Pedido inicial. Pega os dados preencidos previamente
        form = EntryForm(instance=entry)
    else:
        #Dados dp método POST serão atualizados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('movie', args=[movie.id]))
    context = {'entry': entry, 'movie': movie, 'form': form}
    return render(request, 'cine_lists/edit_entry.html', context)

def remove_entry(request, entry_id):
    """"Remove uma anotação existente"""
    entry = Entry.objects.get(id=entry_id)
    movie = entry.movie

    if request.method != 'POST':
        entry.delete()
        return HttpResponseRedirect(reverse('movie', args=[movie.id]))
    context = {'entry': entry, 'movie': movie}
    return render(request, 'cine_lists/remove_entry.html', context)

def remove_movie(request, movie_id):
    """"Remove uma anotação existente"""
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == "POST":
        movie.delete()
        return redirect('movies')
    context = {'movie': movie}
    return render(request, 'cine_lists/remove_movie.html', context)
