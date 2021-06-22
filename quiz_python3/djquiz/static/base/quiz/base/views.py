from django.shortcuts import render

from djquiz.static.base.quiz.base.models import Pergunta


def home(requisicao):
    return render(requisicao, 'base/home.html')


def classificacao(requisicao):
    return render(requisicao, 'base/classificacao.html')


def perguntas(requisicao, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    contexto = {'indice_da_questao': indice, 'pergunta': pergunta}
    return render(requisicao, 'base/game.html', context=contexto)
