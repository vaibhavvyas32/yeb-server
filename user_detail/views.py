from django.shortcuts import render
from rest_framework import viewsets
from user_detail.models import UserDetail
from user_detail.serializers import UserDetailSerializer

# Create your views here.
class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer