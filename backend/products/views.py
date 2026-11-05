from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'is_active', 'min_price', 'max_price']


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = ProductFilter

    search_fields = ['name', 'description', 'category']

    ordering_fields = ['price', 'created_at', 'name']

    ordering = ['-created_at']

