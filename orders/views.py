from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Order

#Vista para devolver todas las ordenes#
def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request,'orders/list_orders.html', context=context)


def create_order(request):
    Order.objects.create(client='Daniel', product='Rogue training socks', payment_method='Cash')
    return HttpResponse('Created Order!!!!')