from django.contrib import admin
from django.urls import include, path
from .views import product, load_product, index

urlpatterns = [
    path('list/', index, name='product_list'),
    path('load/', load_product, name = 'load_product'),
    path('<int:product_id>/', product, name="product" ),
]