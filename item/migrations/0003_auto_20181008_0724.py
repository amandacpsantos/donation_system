# Generated by Django 2.1.1 on 2018-10-08 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_auto_20181007_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Doações',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.AddField(
            model_name='donation',
            name='item',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='item.Item'),
        ),
        migrations.AddField(
            model_name='donation',
            name='taker',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]