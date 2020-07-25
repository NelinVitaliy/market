from django.urls import path
from .views import *

app_name = "shop"

urlpatterns = [
    path('', home_list, name='home_list'),

    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('products-detail/<slug:category_slug>/', get_product_by_category, name='product_by_category'),
    path('product-detail/<slug:slug>/', product_detail, name='product_detail'),

    path('all-products', get_all_products, name='all-products'),
    path('contact', contact_list, name='contact_list'),
    path('wholesalers', wholesalers_list, name='wholesalers_list'),

    # path('', base_list, name='base')
]
