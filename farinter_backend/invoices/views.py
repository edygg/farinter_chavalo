from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models


# Nueva factura
@api_view(["POST", "GET"])
def create_list_invoice(request, format=None):
    if request.method == "POST":
        serializer = serializers.InvoiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        invoices = models.Invoice.objects.all()
        serializer = serializers.CompleteInvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Agregar producto a factura
@api_view(["POST"])
def add_product_to_invoice(request, format=None):
    if request.method == "POST":
        serializer = serializers.InvoiceDetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            invoice = serializer.instance.invoice

            invoice_serializer = serializers.CompleteInvoiceSerializer(invoice)

            return Response(invoice_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Quitar producto a factura
@api_view(["DELETE"])
def remove_product_to_invoice(request, format=None):
    if request.method == "DELETE":
        pass


# Detalle Factura
@api_view(["GET"])
def get_invoice(request, pk, format=None):
    if request.method == "GET":
        invoice = models.Invoice.objects.get(pk=pk)
        serializer = serializers.CompleteInvoiceSerializer(invoice)

        return Response(serializer.data, status=status.HTTP_200_OK)
