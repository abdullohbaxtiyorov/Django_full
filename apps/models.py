import uuid
from django.utils import timezone

from django.db import models
from django.db.models import Model, UUIDField, CharField, ForeignKey, CASCADE, DateTimeField


class Category(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE)
    created_at = DateTimeField()

    # def save(self, *args, **kwargs):
    #     # Vaqtni Toshkent vaqtiga o'zgartiramiz
    #     if not self.created_at:
    #         self.created_at = timezone.localtime(
    #             timezone.now())
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

