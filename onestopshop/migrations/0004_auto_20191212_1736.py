# Generated by Django 3.0 on 2019-12-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestopshop', '0003_auto_20191212_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onestopshop',
            name='price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='onestopshop',
            name='quantity',
            field=models.CharField(max_length=10),
        ),
    ]