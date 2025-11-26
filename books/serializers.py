from .models import Book
from rest_framework import serializers
class Booksserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
        def create(self,validated_data):
            u=User.objects.create_user(**validated_data)
            u.save()
            return u