from django.shortcuts import render
from .models import Travel, UTravel
from .serializers import TravelSerializer, UTravelSerializer
from rest_framework import viewsets


class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class UTravelViewSet(viewsets.ModelViewSet):
    queryset = UTravel.objects.all()
    serializer_class = UTravelSerializer
