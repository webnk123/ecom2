from django.contrib import admin
from .models import (Product, ProductImage,
                    ProductCategory, Review, ReviewImage,
                    DailyReport)


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Review)
admin.site.register(ReviewImage)
admin.site.register(DailyReport)
