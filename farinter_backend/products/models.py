from django.db import models
from django.utils.translation import gettext_lazy as _
from farinter_backend.core import constants as core_constants


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=core_constants.Money.MAX_DIGITS,
        decimal_places=core_constants.Money.DECIMAL_PLACES
    )
    tax = models.ForeignKey('products.Tax', on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Tax(models.Model):
    percentage = models.DecimalField(
        max_digits=core_constants.Money.MAX_DIGITS,
        decimal_places=core_constants.TaxPercentage.DECIMAL_PLACES
    )

    class Meta:
        verbose_name = _("Tax")
        verbose_name_plural = _("Taxes")
