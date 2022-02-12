import queue
from django.shortcuts import render
from rest_framework import viewsets
from .models import Paradigm, Programmer, Language
from .serializers import ParadigmSerializer, ProgrammerSerializer, LanguageSerializer

# Create your views here.

class LanguageList(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmList(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerList(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer