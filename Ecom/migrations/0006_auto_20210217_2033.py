# Generated by Django 3.1.6 on 2021-02-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0005_auto_20210217_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField()
        ),
    ]
