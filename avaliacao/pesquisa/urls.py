from django.conf.urls import url

from . import views

app_name = 'pesquisa'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^selecionarCurso$', views.selecionarCurso, name='selecionarCurso'),
    url(r'^avaliarCurso$', views.avaliarCurso, name='avaliarCurso'),
    url(r'^registrarAvaliacao$', views.registrarAvaliacao, name='registrarAvaliacao'),
    url(r'^cadastrarCurso$', views.cadastrarCurso, name='cadastrarCurso'),
    url(r'^cursosAvaliados$', views.cursosAvaliados, name='cursosAvaliados'),
]
