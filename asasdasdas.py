import os

from datetime import datetime
from email.policy import default
from inspect import trace
from os.path import exists
from unicodedata import category

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product, Category, User
from django.db import transaction
from django.db.models import Q, F, Min, OuterRef, Subquery, Sum, Count

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
# obj = Product.objects.in_bulk()
# obj = Product.objects.latest('name')
# obj1 = Product.objects.order_by()


# min_price_subquery = Product.objects.values('price').order_by('price')[:1]
# min_price_subquery = Product.objects.values('price').aggregate(Min('price'))['price__min']
# Product.objects.update(price=F('price') + Subquery(min_price_subquery))

# products = Product.objects.values('name').annotate(total_price=Sum('price'))


# res = Product.objects.values(c_name=F('category__name'))
# for i in res:
#     print(i)


# res = Product.objects.values('name', c_name=F('category__name')).annotate(price=Sum('price'),count=Count('name'))
# user = User.objects.filter(date_joined__year=2020)
res = Product.objects.filter(name__contains='a',
                             price__range=(2000,3500),
                             description__isnull=False)

print(res)
