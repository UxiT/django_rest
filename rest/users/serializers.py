from rest_framework import serializers
from users.models import ModelUser


class UserDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ModelUser
        fields = '__all__'
