from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def movie(request):
    return render(request, 'index.html')

def nav_view(request):
    return render(request, 'nav.html')

def serie(request):
    series = {
        'serie':Serie.objects.all()
    }
    
    return render(request, 'serie/serie.html', series)


def elenco(request):  
    elencos = {
        'elenco':Elenco.objects.all()
    }
    
    return render(request, 'elenco/elenco.html', elencos)


def diretor(request):
    diretores = {
        'diretor':Diretor.objects.all()
    }
    
    return render(request, 'diretor/diretor.html', diretores)


def filme(request):
    filmes = {
        'filme':Filme.objects.all()
    }
    
    return render(request, 'filme/filme.html', filmes)


def ator(request):
    atores = {
        'ator':Ator.objects.all()
    }
    
    return render(request, 'ator/ator.html', atores)