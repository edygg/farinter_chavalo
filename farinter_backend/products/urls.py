from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import generics

from . import models
from . import serializers


urlpatterns = [
    path(
        "",
        generics.ListCreateAPIView.as_view(
            queryset=models.Product.objects.all(),
            serializer_class=serializers.ProductSerializer
        ),
        name='products'
    ),
    path(
        "taxes/",
        generics.ListCreateAPIView.as_view(
            queryset=models.Tax.objects.all(),
            serializer_class=serializers.TaxSerializer
        ),
        name='product-taxes'
    ),
]

app_name = "products"
urlpatterns = format_suffix_patterns(urlpatterns)
