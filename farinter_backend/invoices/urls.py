from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.create_list_invoice),
    path("add-product/", views.add_product_to_invoice),
    path("<int:pk>/", views.get_invoice),

]

app_name = "invoices"
urlpatterns = format_suffix_patterns(urlpatterns)
