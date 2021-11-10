from django.urls import path
from .views import current_user, UserCreate, UsersList, UserEdit

urlpatterns = [
    path('current-user/', current_user),
    path('users/create/', UserCreate.as_view()),
    path('users/list/', UsersList.as_view()),
    path('users/edit/<int:pk>', UserEdit.as_view())
]