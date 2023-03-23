from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('pagina principal')

def details(request, question_id):
    return HttpResponse(f'estas viendo los detalles de {question_id}')

def results(request, question_id):
    return HttpResponse(f'estas viendo los resultados de {question_id}')

def vote(request, question_id):
    return HttpResponse(f'estas viendo los votes de {question_id}')