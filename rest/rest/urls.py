from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path("api/v1/token-auth/", obtain_jwt_token),
    path('core/', include('core.urls'))
]
