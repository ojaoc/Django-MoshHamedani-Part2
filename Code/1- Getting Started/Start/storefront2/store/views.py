from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Product
from .serializers import ProductSerializer


@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)

    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product_obj = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product_obj)

    return Response(serializer.data)