from django.shortcuts import render
import datetime
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]

    context = {'title': title, 'products': products, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):

    title = 'продукты'
    links_menu = ProductCategory.objects.all()


    if pk is not None:
        if pk == 0:
            products = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': get_basket(request.user),
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    context = {'title': 'Продукты', 'links_menu': links_menu, 'same_products': same_products, 'basket': get_basket(request.user),}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html', context)
