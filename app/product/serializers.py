from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Product, ProductType
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    sku = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'prodType', 'product_name', 'field1', 'field2', 'field3', 'sku', 'stock']
        read_only_fields = ('id',)

    def get_sku(self, Product):
        fields = ""
        # if(Product.id != ''):
        #     my_str = str(Product.id).replace(" ", "")
        #     fields += my_str[:3] + "-"
        if(Product.prodType != ''):
            my_str = Product.prodType.replace(" ", "")
            fields += my_str[:3] + "-"
        if(Product.product_name != ''):
            my_str = Product.product_name.replace(" ", "")
            fields += my_str[:3] + "-"
        if(Product.field1 != ''):
            my_str =  Product.field1.replace(" ", "")
            fields += my_str[:3] + "-"
        if(Product.field2 != ''):
            my_str =  Product.field2.replace(" ", "")
            fields += my_str[:3] + "-"
        if(Product.field3 != ''):
            my_str =  Product.field3.replace(" ", "")
            fields += my_str[:3] + "-"
     
        return fields


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = ['id', 'prodType', 'field1_name', 'field2_name', 'field3_name']
        read_only_fields = ('id',)
