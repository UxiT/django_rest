from rest_framework import serializers
from users.models import ModelUser


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = '__all__'
