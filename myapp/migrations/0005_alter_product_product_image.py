# Generated by Django 4.1.1 on 2022-09-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_productimage_product_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ManyToManyField(blank=True, to='myapp.productimage'),
        ),
    ]