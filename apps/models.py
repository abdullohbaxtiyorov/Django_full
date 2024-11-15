import uuid
from datetime import timezone

from django.db import models
from django.db.models import Model, UUIDField, CharField, ForeignKey, CASCADE, DateTimeField, ImageField


class Category(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE)
    created_at = DateTimeField(auto_now=True)
    photo = ImageField(upload_to="apps/product/%Y/%m/%d",null=True, blank=True)

    def __str__(self):
        return self.name
