from django.contrib import admin
from django.db import connections

from apps.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.save()

        with connections['db_2'].cursor() as cursor:
            cursor.execute("INSERT INTO apps_product(name,price) VALUES (%s,%s);", [obj.name, obj.price])