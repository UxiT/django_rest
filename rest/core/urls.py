from django.urls import path
from .views import current_user, UserCreate, UsersList

urlpatterns = [
    path('current-user/', current_user),
    path('users/create', UserCreate.as_view()),
    path('users/list', UsersList.as_view())
]