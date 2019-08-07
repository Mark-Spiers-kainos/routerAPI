from django.shortcuts import render
from rest_framework import viewsets
from .models import Application
from .serializer import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
