# Generated by Django 3.1.5 on 2021-01-23 18:13

from django.conf import settings
from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='funcionarios',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
