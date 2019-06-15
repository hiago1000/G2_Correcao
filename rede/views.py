from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView
from .models import *
from .forms import PublicacaoForm, ComentarioForm
from django.http import HttpResponse


def inicio(request):
    colaborador = Colaborador.objects.get(usuario=request.user)
    seguidores = colaborador.seguidores.all()
    publicacoes = Publicacao.objects.filter(autor__in=seguidores)

    return render(request, 'rede/inicio.html', {'publicacoes': publicacoes})

def perfil(request, nome):
    try:
        colaborador = Colaborador.objects.get(usuario__username=nome)
        publicacoes = Publicacao.objects.filter(autor=colaborador)
    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')
    
    return render(request, 'rede/perfil.html', {'publicacoes': publicacoes, 'colaborador': colaborador})

def seguir(request, id_colaborador):
    try:
        colaborador = Colaborador.objects.get(usuario=request.user)
        cara_quero_seguir = Colaborador.objects.get(pk=id_colaborador)
        colaborador.seguidores.add(cara_quero_seguir)

    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')
    
    return render(request, 'rede/sucesso_seguir.html', {'famosinho': cara_quero_seguir})

class HomePageView(TemplateView):
    template_name = 'rede/home.html'


class PublicacaoView(FormView):
    template_name = 'rede/publicar.html'
    form_class = PublicacaoForm

    def form_valid(self, form):
        dados = form.clean()
        colaborador = Colaborador.objects.get(usuario=self.request.user)
        publicacao = Publicacao(texto=dados['texto'], autor=colaborador)
        publicacao.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inicio')


class ComentarioView(FormView):
    template_name = 'rede/comentar.html'
    form_class = ComentarioForm


    def form_valid(self, form):
        dados = form.clean()
        publicacao = Publicacao.objects.get(pk=id)
        colaborador = Colaborador.objects.get(usuario=self.request.user)
        comentario = Comentario(texto=dados['texto'], autor=colaborador)
        comentario.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inicio')


