from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ProductSerializer

from core.models import Product



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
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #   return self.queryset.filter(brand=self.request.user).order_by('-brand')

