from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.create_invoice),
]

app_name = "invoices"
urlpatterns = format_suffix_patterns(urlpatterns)
