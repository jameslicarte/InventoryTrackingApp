from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Product, ProductType
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

    sku = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'prodType', 'product_name', 'field1', 'field2', 'field3', 'sku', 'stock', 'updated_date']
        read_only_fields = ('id','updated_date')

    def get_sku(self, Product):
        fields = ""
        if(Product.id != ''):
            fields += str(Product.id).replace(" ","") + '/'
        if(Product.prodType != ''):
            fields += Product.prodType.replace(" ","") + '/'
        if(Product.product_name != ''):
            fields += Product.product_name.replace(" ","") + '/'
        if(Product.field1 != ''):
            fields += Product.field1.replace(" ","") + '/'
        if(Product.field2 != ''):
            fields += Product.field2.replace(" ","") + '/'
        if(Product.field3 != ''):
            fields += Product.field3.replace(" ","") + '/'
        
        return fields

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductType
        fields = ['id', 'prodType', 'field1_name', 'field2_name', 'field3_name']
        read_only_fields = ('id',)



