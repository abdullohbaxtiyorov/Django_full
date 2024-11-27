# from django.contrib.auth.models import AbstractUser
# from django.db.models import Model, CharField, IntegerField, BooleanField, Manager, QuerySet
#
#
# class ProductManager(Manager):
#
#     def get_queryset(self):
#         return super().get_queryset()
#
#
# class ProductQuerySet(QuerySet):
#     def top_products(self, min_price):
#         return self.filter(is_premium=True, price__gte=min_price)
#
#     def between_price(self, min_price, max_price):
#         return self.filter(is_premium=False, price__gte=min_price, price__lte=max_price)
#
#
# class User(AbstractUser):
#     pass
#
# class Product(Model):
#     name = CharField(max_length=255)
#     price = IntegerField(db_default=0)
#     is_premium = BooleanField(db_default=False)
#     objects = Manager()
#     cheap = ProductManager().from_queryset(ProductQuerySet)()
#
#
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, PositiveSmallIntegerField, TextField,CharField

class User(AbstractUser):
    pass

class Product(Model):
    name = CharField(max_length=255)
    price = PositiveSmallIntegerField(db_default=0)
    # description = TextField(null=True, blank=True)
