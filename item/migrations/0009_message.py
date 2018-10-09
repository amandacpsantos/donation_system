# Generated by Django 2.1.2 on 2018-10-08 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20181008_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=254)),
                ('to_email', models.EmailField(max_length=254)),
                ('subject', models.TextField(max_length=45)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
