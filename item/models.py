from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.conf import settings


class Status(models.Model):
    type = models.CharField(max_length=45)

    def __str__(self):
        return self.type



class Category(models.Model):
    type = models.CharField(max_length=45)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Categories"


class Item(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    donor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Itens"