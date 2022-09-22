from rest_framework import serializers
from .models import Product, ProductCategory, Review
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #get product_images.url
    product_images = serializers.StringRelatedField(many=True)
    product_category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['name', 'description','price', 'product_images','product_category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_name']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
        write_only_fields = ['password',]

    # hash passwords of new users
    def validate_password(self, value: str) -> str:
        return make_password(value)

'''
sqlite objects of:

-USER CREATED AT /ADMIN

        hashed_password
           V

1|pbkdf2_sha256$390000$XHVgoaOZZLekwBAPh42SLN$NsHFxjAFP3SrgGFG9WIvxZpXlIMzPipv4GmntO/5muY=
|2022-09-17 16:20:22.847105|1|admin|||1|1|2022-09-17 15:46:42.969297|

-USER CREATED BY USER SERIALIZER WIHTOUT validate_password()

plaintext password
    V           

3|testing||0|testing|||0|1|2022-09-17 16:20:56.055316|
'''

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    #get product_images.url
    author = serializers.StringRelatedField(many=False)
    review_images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Review
        fields = ['author','review_body', 'review_images']

