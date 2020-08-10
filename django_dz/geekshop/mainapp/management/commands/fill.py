import json
import os
from django.core.management import BaseCommand
from geekshop.settings import BASE_DIR
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser


def load_json(file_name):
    with open(os.path.join(BASE_DIR, file_name + '.json')) as file_json:
        return json.load(file_json)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = load_json('categories')

        ProductCategory.objects.all().delete()

        for new_cat in categories:
            obj_cat = ProductCategory.objects.create(**new_cat)

        
        products = load_json('products')

        Product.objects.all().delete()

        for new_prod in products:
            cat_name = new_prod['category']
            cur_cat = ProductCategory.objects.get(name=cat_name)
            new_prod['category'] = cur_cat
            obj_prod = Product(**new_prod)
            obj_prod.save()


        ShopUser.objects.create_superuser('django', 'gb@local', 'geekbrains', age=33)

