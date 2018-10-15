from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .enum_collection import STATUS_CHOICES, CATEGORY_CHOICES


class Item(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=200)
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='REGISTERED',
        editable=False,
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='FOOD',
    )
    donor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        editable=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Itens"
        verbose_name = "Item"


class Donation(models.Model):
    date = models.DateField(auto_now=True, editable=False)
    taker = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name_plural = "Doações"
        verbose_name = "Doação"


class Message(models.Model):
    # from_email = models.EmailField()
    to_email = models.EmailField()
    subject = models.TextField(max_length=45)
    date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "Mensagens"
        verbose_name = "Mensagem"
