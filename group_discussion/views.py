from django.shortcuts import render
from group_discussion.models import GD, StdGD
from group_discussion.serializers import GdSerializer, StdGDSerializer
from rest_framework import viewsets

# Create your views here.
class GDViewSet(viewsets.ModelViewSet):
    queryset = GD.objects.all()
    serializer_class = GdSerializer

class StdGDViewSet(viewsets.ModelViewSet):
    queryset = StdGD.objects.all()
    serializer_class = StdGDSerializer