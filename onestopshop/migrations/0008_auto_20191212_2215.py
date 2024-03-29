# Generated by Django 3.0 on 2019-12-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestopshop', '0007_auto_20191212_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onestopshop',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='onestopshop',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='onestopshop',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
