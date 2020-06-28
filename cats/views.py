from django.shortcuts import render
from django.http import HttpResponse
from .models import Cats
from rest_framework import viewsets
from .serializers import CatsSerializer


def index(request):
    return HttpResponse("Placeholder")


class CatsViewSet(viewsets.ModelViewSet):
    """
    Get a list of all the Cats
    """
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
