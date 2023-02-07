from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products, Category
from products.forms import ProductForm

# Aca creamos los productos
def create_product(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }
        return render(request, 'products/create_product.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
          Products.objects.create(
            name = form.cleaned_data['name'],
            price = form.cleaned_data['price'],
            stock = form.cleaned_data['stock'],
          )
          context = {
            'message': 'Product created successfully'
          }
          
          return render(request, 'products/create_product.html', context=context)            
        else:
            #Aca tenemos que manejar el error#
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create_product.html', context=context)
            #Aca tenemos que manejar el error#
             

#Para ver la lista de los productos creados#
def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__contains=search)
    else:
        products = Products.objects.all()
    #Para mostrar los productos los metemos en el contexto#
    context = {
        'products': products
    }
    return render(request, 'products/list_products.html', context=context)


def create_category(request, name):
    new_category = Category.objects.create(name= name)
    print(new_category)
    return HttpResponse('The category was created!!')
    

def list_categories(request):
    all_categories = Category.objects.all()
    print(all_categories)
    context = {
        'categories': all_categories
    }
    return render(request,'categories/list_categories.html', context=context )