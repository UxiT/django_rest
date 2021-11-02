from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.serializers import UserDetailSerializer
from users.models import ModelUser
from users.permissions import IsOwnerReadOnly
import rest_framework as rest


# Create your views here.
class UserPagination(rest.pagination.PageNumberPagination):
    page_size_query_param = "size"
    page_query_param = "page"
    max_page_size = 20


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = ModelUser.objects.all()
    pagination_class = UserPagination


class UserEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = ModelUser.objects.all()


@api_view(["GET"])
def get_user(request, pk):
    obj = ModelUser.objects.get(pk=pk)
    serializer = UserDetailSerializer(obj, many=False)
    return Response(serializer.data)
