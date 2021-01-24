# Generated by Django 3.1.5 on 2021-01-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionarios',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='funcionarios',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='is_superuser',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
