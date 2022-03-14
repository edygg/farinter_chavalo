from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers


# Nueva factura
@api_view(["POST"])
def create_invoice(request, format=None):
    if request.method == "POST":
        serializer = serializers.InvoiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Agregar producto a factura
@api_view(["POST"])
def add_product_to_invoice(request, format=None):
    pass


# Quitar producto a factura
# Listar facturas
# Detalle Factura

