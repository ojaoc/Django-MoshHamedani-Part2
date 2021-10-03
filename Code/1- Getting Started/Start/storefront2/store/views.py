from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        queryset = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT"])
def product_detail(request, id):
    product_obj = get_object_or_404(Product, pk=id)
    if request.method == "GET":
        serializer = ProductSerializer(product_obj)

        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    return Response("ok")
