from django.shortcuts import render
from rest_framework import generics
from users.serializers import UserDetailSerializer, UserListSerializer
from users.models import ModelUser
import rest_framework as rest


# Create your views here.
class UserPagination(rest.pagination.PageNumberPagination):
    page_size_query_param = "size"
    page_query_param = "page"
    max_page_size = 20


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = ModelUser.objects.all()
    pagination_class = UserPagination


class UserEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = "__all__"
