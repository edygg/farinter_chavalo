from rest_framework import serializers
from . import models


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = ["id", "issue_date", "client_name"]
