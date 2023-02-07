from django.contrib import admin

from products.models import Products, Category

#Agregar modelos al admin site#
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ('name', 'price', 'stock')
    list_filter = ('stock', 'price')
    search_fields = ('name',)



admin.site.register(Category)




