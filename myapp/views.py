from .models import Product, ProductCategory, Review
from .serializers import (ProductSerializer, CategorySerializer,
                          UserSerializer, ReviewSerializer)

from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.authtoken.models import Token




class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing products. cached with redis.
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class ProductByCategory(generics.ListAPIView):
    """
    A view for viewing products by category. cached with redis.
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        category = self.kwargs['cat']
        return Product.objects.filter(product_category__category_name=category)

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AllCategories(generics.ListAPIView):
    """
    A view for listing all categories. cached with redis.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class UserList(generics.CreateAPIView):
    """
    A view for creating a user
    """
    serializer_class = UserSerializer



class ReviewsByProduct(generics.ListAPIView):
    """
    A view for viewing reviews for product. cached with redis.
    """
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """
        This view should return a list of all the reviews for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id']
        return Review.objects.filter(author__id=id).filter(is_moderated=True)

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

