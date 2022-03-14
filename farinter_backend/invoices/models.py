from django.db import models
from django.utils.translation import gettext_lazy as _
from farinter_backend.core import constants as core_constants


class Invoice(models.Model):
    issue_date = models.DateField(auto_now_add=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    subtotal = models.DecimalField(
        max_digits=core_constants.Money.MAX_DIGITS,
        decimal_places=core_constants.Money.DECIMAL_PLACES,
        default=core_constants.Money.ZERO
    )
    taxes = models.DecimalField(
        max_digits=core_constants.Money.MAX_DIGITS,
        decimal_places=core_constants.Money.DECIMAL_PLACES,
        default=core_constants.Money.ZERO
    )
    grand_total = models.DecimalField(
        max_digits=core_constants.Money.MAX_DIGITS,
        decimal_places=core_constants.Money.DECIMAL_PLACES,
        default=core_constants.Money.ZERO
    )

    class Meta:
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey("invoices.Invoice", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(
        max_digits=core_constants.Money.MAX_DIGITS,
        decimal_places=core_constants.Money.DECIMAL_PLACES,
        default=core_constants.Money.ZERO
    )
    subtotal = models.DecimalField(
        max_digits=core_constants.Money.MAX_DIGITS,
        decimal_places=core_constants.Money.DECIMAL_PLACES,
        default=core_constants.Money.ZERO
    )

    class Meta:
        verbose_name = _("Invoice detail")
        verbose_name_plural = _("Invoice details")
