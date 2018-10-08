from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Item(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=45, default='Disponível', null=True, blank=True)
    category = models.CharField(max_length=45, null=True, blank=True)
    donor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Itens"


class Donation(models.Model):
    date = models.DateField(auto_now=True)
    taker = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, editable=False)


    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name_plural = "Doações"

