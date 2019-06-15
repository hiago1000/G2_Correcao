from django.urls import path
from .views import HomePageView, inicio, PublicacaoView, perfil, seguir, ComentarioView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inicio/', inicio, name='inicio'),
    path('publicar/', PublicacaoView.as_view(), name='publicar'),
    path('perfil/<str:nome>/', perfil, name='publicar'),
    path('seguir/<int:id_colaborador>', seguir, name='seguir'),
    path('comentario/publicacao/<int:id>', ComentarioView.as_view(), name='comentar')

]
