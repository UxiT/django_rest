from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework import generics
from core.models import MyUser


@api_view(["GET"])
def current_user(request):
    # Determine cuurent user by their token and return their data
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserCreate(APIView):
    
    permission_classes = (permissions.AllowAny,)
    

    def post(self, request, format=None):
        serialiser = UserSerializerWithToken(data=request.data)

        if serialiser.is_valid():
            serialiser.save() 
            return Response(serialiser.data, status = status.HTTP_201_CREATED)

        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)



class UsersList(generics.ListAPIView):
    serializer_class = UserSerializerWithToken
    queryset = MyUser.objects.all()
    permission_classes=(permissions.AllowAny,)



