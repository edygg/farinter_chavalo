from rest_framework import serializers
from . import models


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = ["id", "issue_date", "client_name"]


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceDetail
        fields = ["id", "invoice", "product", "quantity", "discount"]
