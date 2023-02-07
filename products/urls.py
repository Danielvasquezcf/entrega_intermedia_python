from django.urls import path, include
from products.views import create_product, list_products, list_categories, create_category

urlpatterns = [
     #Crear producto#
    path('create-product/', create_product),
    #listar los productos creados#
    path('list-products/', list_products),
    #Listar las categorias creadas#
    path('list-categories/', list_categories),
    #Crear Categorias#
    path('create-category/<str:name>/', create_category),
]