# Generated by Django 4.1.1 on 2022-09-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_product_image_product_product_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(blank=True, to='myapp.productcategory'),
        ),
    ]