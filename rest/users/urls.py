from django.contrib import admin
from django.urls import path, include
from users.views import *

app_name = "users"
urlpatterns = [
    path("user/create/", UserCreateView.as_view()),
    path("list/", UserListView.as_view()),
    path("user/edit/<int:pk>", UserEdit.as_view())
]
