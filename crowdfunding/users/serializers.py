from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email =serializers.EmailField()
    password = serializers.CharField(write_only = True)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    profile_image = serializers.URLField(default="https://via.placeholder.com/150", max_length=200)
    is_active = serializers.BooleanField(default=True)
  

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)  
#accept the password and won't save it but creata # about it. password is scrambled so its illegible.

# class ProfileUserSerializer(serializers.Serializer):  #profile
#     username = serializers.CharField(max_length=200)
#     email =serializers.EmailField()
#     first_name = serializers.CharField(max_length=150)
#     last_name = serializers.CharField(max_length=150)
#     profile_image = serializers.URLField(default="https://via.placeholder.com/150", max_length=200)

class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

