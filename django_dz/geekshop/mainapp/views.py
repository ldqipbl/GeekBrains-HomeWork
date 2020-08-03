from django.shortcuts import render
from mainapp.models import Product


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = Product.objects.all()
    context = {
        'title': 'Продукты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)

def products_all(request):
    links_menu = [
            {'href': 'products_all', 'name': 'все'},
            {'href': 'products_home', 'name': 'дом'},
            {'href': 'products_office', 'name': 'офис'},
            {'href': 'products_modern', 'name': 'модерн'},
            {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'Продукты все',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)

def products_home(request):
    links_menu = [
            {'href': 'products_all', 'name': 'все'},
            {'href': 'products_home', 'name': 'дом'},
            {'href': 'products_office', 'name': 'офис'},
            {'href': 'products_modern', 'name': 'модерн'},
            {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'Продукты для дома',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)

def products_office(request):
    links_menu = [
            {'href': 'products_all', 'name': 'все'},
            {'href': 'products_home', 'name': 'дом'},
            {'href': 'products_office', 'name': 'офис'},
            {'href': 'products_modern', 'name': 'модерн'},
            {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'Продукты для офиса',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)

def products_modern(request):
    links_menu = [
            {'href': 'products_all', 'name': 'все'},
            {'href': 'products_home', 'name': 'дом'},
            {'href': 'products_office', 'name': 'офис'},
            {'href': 'products_modern', 'name': 'модерн'},
            {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'Продукты модерн',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)

def products_classic(request):
    links_menu = [
            {'href': 'products_all', 'name': 'все'},
            {'href': 'products_home', 'name': 'дом'},
            {'href': 'products_office', 'name': 'офис'},
            {'href': 'products_modern', 'name': 'модерн'},
            {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'Продукты классика',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)



def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)
