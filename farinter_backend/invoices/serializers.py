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


class CompleteInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = '__all__'

    def to_representation(self, instance):
        representation = dict()
        invoice_rows = list()

        for invoice_detail in instance.invoicedetail_set.all():
            invoice_detail_representation = dict(
                id=invoice_detail.id,
                product=dict(
                    name=invoice_detail.product.name,
                    unit_price=invoice_detail.product.price,
                    tax=invoice_detail.product.tax.percentage,
                ),
                quantity=invoice_detail.quantity,
                discount=invoice_detail.discount,
                subtotal=invoice_detail.subtotal,
            )
            invoice_rows.append(invoice_detail_representation)


        representation.update(dict(
            id=instance.id,
            issue_date=instance.issue_date,
            client_date=instance.client_name,
            subtotal=instance.subtotal,
            taxes=instance.taxes,
            grand_total=instance.grand_total,
            invoice_rows=invoice_rows,
        ))




        return representation
