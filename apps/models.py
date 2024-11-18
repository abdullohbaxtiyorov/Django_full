import uuid
from datetime import timezone

from django.db import models
from django.db.models import Model, UUIDField, CharField, ForeignKey, CASCADE, DateTimeField, ImageField, IntegerField


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE)
    created_at = DateTimeField(auto_now=True)
    photo = ImageField(upload_to="apps/product/%Y/%m/%d",null=True, blank=True)
    price = IntegerField(default=0)

    def __str__(self):
        return self.name
