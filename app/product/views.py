from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ProductSerializer, ProductTypeSerializer
from rest_framework import generics

from core.models import Product
from core.models import ProductType


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#views for product
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

#views for productType
class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.AllowAny]
