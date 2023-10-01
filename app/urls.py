from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.filme, name='movie'),
    path('nav.html', views.nav_view, name='nav'),
    path('serie/', views.serie, name="serie"),
    path('elenco/', views.elenco, name="elenco"),
    path('diretor/', views.diretor, name="diretor"),
    path('filme/', views.filme, name="filme"),
    path('ator/', views.ator, name="ator"),
]