from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    SKU = models.CharField(max_length=50, blank=True,  unique=True)
    is_active = models.BooleanField(default=False)
    product_images = models.ManyToManyField('ProductImage', blank=True)
    product_category = models.ManyToManyField('ProductCategory', blank=True)


    def __str__(self):
        return self.name



class ProductImage(models.Model):
    image = models.ImageField(upload_to ='images')

    def __str__(self):
        return self.image.url


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name



# TODO
'''
class Order(models.Model):
    owner = models.ForeignKey('auth.User', related_name='cart', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=250,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200, blank=True, null=True)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.product__price * self.quantity

    def __str__(self):
        return self.name
'''

class Review(models.Model):
    author = models.ForeignKey('auth.User', related_name='review', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    review_body = models.TextField()
    review_images = models.ManyToManyField('ReviewImage', blank=True)
    is_moderated = models.BooleanField(default=False)



class ReviewImage(models.Model):
    image = models.ImageField(upload_to ='images')

    def __str__(self):
        return self.image.url


class DailyReport(models.Model):
    total_products = models.PositiveIntegerField()
    total_reviews = models.PositiveIntegerField()
    total_categories = models.PositiveIntegerField()