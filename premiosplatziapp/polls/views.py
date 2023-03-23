# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", { "latest_question_list": latest_question_list })

def details(request, question_id):
    return HttpResponse(f'estas viendo los detalles de {question_id}')

def results(request, question_id):
    return HttpResponse(f'estas viendo los resultados de {question_id}')

def vote(request, question_id):
    return HttpResponse(f'estas viendo los votes de {question_id}')