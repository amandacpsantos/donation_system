# Generated by Django 2.1.2 on 2018-10-08 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_auto_20181008_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='from_email',
        ),
    ]
