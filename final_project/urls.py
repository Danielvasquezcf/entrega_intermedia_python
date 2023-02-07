
from django.contrib import admin
from django.urls import path, include
from final_project.views import hello, actual_time, age_view, name, home, index



urlpatterns = [
    path('admin/', admin.site.urls),
    #INDEX#
    path('', index, name='index'),
    path('hello/', hello),
    path('today/', actual_time),
    #Cuando queremos que nos mande parametros del front <>#
    path('age/<int:age>/', age_view),
    #Cuando es string ya toma el dato por defecto a diferencia del int#
    path('name/<name>/', name),
    path('home/', home),

    path('products/', include('products.urls')), #el primer products es el prefijo que se le pone de base 
    path('orders/', include('orders.urls')),
   
]
