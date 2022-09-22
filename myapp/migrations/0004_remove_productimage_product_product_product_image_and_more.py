# Generated by Django 4.1.1 on 2022-09-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ManyToManyField(blank=True, related_name='product_img', to='myapp.productimage'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
