# Generated by Django 3.1.6 on 2021-02-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0002_auto_20210215_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]