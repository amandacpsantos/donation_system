from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(User):
    phone = models.CharField(max_length=11, blank=True, null=True)

    # 1 é o id_grupo que fiz no painel admin. Ainda não sei como passar chamando função.
    groups = 1

    def __str__(self):
        return self.username


    class Meta:
        verbose_name_plural = "Names"