from rest_framework import serializers
from .models import CustomUser

class CustomerUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email =serializers.EmailField()

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)  #accept the password and won't save it but creata # about it. password is scrambled so its illegible.