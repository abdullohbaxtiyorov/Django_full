import os
from datetime import datetime
from inspect import trace

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product, Category
from django.db import transaction
from django.db.models import Q, F
# s = 'texnika'
# product = Product.objects.filter(name__icontains= 'texnika').values('name')
# category = Category.objects.filter(name__icontains='texnika').values('name')
# r = category.union(product)
# for i in r:
#     print(i['name'])

product = Product.objects.select_for_update().filter(category_id=2)

# with transaction.atomic():
#     for product in product:
#         print(product.name)

# obj, create = Product.objects.get_or_create(name='hp',defaults={'category_id': 1})
# print(obj)

# obj = Product.objects.filter(Q(category__name='meva') | Q(name = 'banan')).update(price= 25000)
# print(obj)

# obj = Product.objects.filter(category__name='meva').update(price= F('price')*2)
# print(Product.objects.filter(category_id=2).count())
# print(len(Product.objects.filter(category_id=2)))
obj = Product.objects.in_bulk()
for i,k in obj.items():
    print(i,k.name)