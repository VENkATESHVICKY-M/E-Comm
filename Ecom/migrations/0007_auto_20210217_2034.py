# Generated by Django 3.1.6 on 2021-02-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0006_auto_20210217_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=True),
        ),
    ]
