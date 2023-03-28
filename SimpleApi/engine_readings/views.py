from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Engine, Reading
from .serializers import EngineSerializer
from rest_framework.generics import ListAPIView
#
import pandas as pd
from django_pandas.io import read_frame

def read_and_store_data(file_path):
    df = pd.read_excel(file_path, sheet_name='Sheet1')

    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
        # Buscar o crear el objeto Engine
        engine, _ = Engine.objects.get_or_create(name='DanyMotors')

        # Crear y guardar el objeto Reading
        reading = Reading(value=row['value'], engine=engine)
        reading.save()


# Create your views here.

class EngineView(ListAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
