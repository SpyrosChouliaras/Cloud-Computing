from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Movies
from .serializers import MoviesSerializer
class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
