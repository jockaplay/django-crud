from django.urls import path
from .views import list_products, create_products

urlpatterns = [
    path('', list_products, name='list_products'),
    path('new', create_products, name='create_products'),
]