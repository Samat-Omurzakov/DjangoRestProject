from django.db.models import Avg, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import ProductSerializers, CategorySerializers, ReviewSerializers, ProductReviewSerializers
from product.models import Category, Product, Review


# Create your views here.
@api_view(['GET'])
def category_api_view(request):
    category = Category.objects.all()
    data_dict = CategorySerializers(category, many=True).data
    products_count = Category.objects.aggregate(products_count=Count('products_count'))
    return Response(data=[data_dict, products_count])


@api_view(['GET'])
def product_api_view(request):
    product = Product.objects.all()
    data_dict = ProductSerializers(product, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def review_api_view(request):
    review = Review.objects.all()
    data_dict = ReviewSerializers(review, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'errors': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data_dict = CategorySerializers(category, many=False).data
    return Response(data=data_dict)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'errors': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data_dict = ProductSerializers(product, many=False).data
    return Response(data=data_dict)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'errors': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data_dict = ReviewSerializers(review, many=False).data
    return Response(data=data_dict)


@api_view(['GET'])
def products_reviews_api_view(request):
    product_review = Product.objects.all()
    avarage_stars = Review.objects.aggregate(avgarage_stars=Avg('stars'))
    data_dict = ProductReviewSerializers(product_review, many=True).data
    return Response(data=[data_dict, avarage_stars])
