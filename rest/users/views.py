from django.shortcuts import render
from rest_framework import generics
from users.serializers import UserDetailSerializer, UserListSerializer
from users.models import ModelUser

# Create your views here.


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = ModelUser.objects.all()
