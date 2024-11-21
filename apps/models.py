import uuid
from datetime import timezone

from django.db import models
from django.db.models import Model, UUIDField, CharField, ForeignKey, CASCADE, DateTimeField, ImageField, IntegerField, \
    TextField
from django.contrib.auth.models import AbstractUser
from psycopg2.errorcodes import ACTIVE_SQL_TRANSACTION


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE)
    created_at = DateTimeField(auto_now=True)
    photo = ImageField(upload_to="apps/product/%Y/%m/%d", null=True, blank=True)
    price = IntegerField(default=0)
    user = ForeignKey('apps.User', on_delete=CASCADE)
    description = TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    pass


