from django.contrib import admin

from orders.models import Order

#Agregar modelos al admin site#
admin.site.register(Order)
