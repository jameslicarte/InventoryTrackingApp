from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Product
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','name']
        extra_kwargs = {'password': { 'write_only': True,'min_length': 5}}
    
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user =  User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'brand', 'prodType', 'color', 'size']
        read_only_fields = ('id',)