from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """Faz o logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

