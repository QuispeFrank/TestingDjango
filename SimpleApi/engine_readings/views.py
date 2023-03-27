from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Engine
from .serializers import EngineSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class EngineView(ListAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
