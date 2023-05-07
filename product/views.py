from django.db.models import Avg, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import ProductSerializers, CategorySerializers, ReviewSerializers, ProductReviewSerializers
from product.models import Category, Product, Review


# Create your views here.
@api_view(['GET', 'POST'])
def product_api_view(request):
    if request.method == 'GET':
        """ Get List of objects """
        product = Product.objects.all()
        """ Serialize (Reformat) objects to dict """
        data_dict = ProductSerializers(product, many=True).data
        """ Return data by JSON file """
        return Response(data=data_dict)
    elif request.method == 'POST':
        """ Read Body """
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category = request.data.get('category')
        category_id = request.data.get('category_id')
        """ Create Product """
        product = Product.objects.create(title=title, description=description, price=price, category=category,
                                         category_id=category_id)
        """ Return Response """
        return Response(data=ProductSerializers(product).data)


@api_view(['GET', "POST"])
def category_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        data_dict = CategorySerializers(category, many=True).data
        products_count = Category.objects.aggregate(products_count=Count('products_count'))
        return Response(data=[data_dict, products_count])
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializers(category).data)


@api_view(['GET', 'Post'])
def review_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data_dict = ReviewSerializers(review, many=True).data
        return Response(data=data_dict)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
        review = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=ReviewSerializers(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'errors': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = CategorySerializers(category, many=False).data
        return Response(data=data_dict)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        return Response(data=CategorySerializers(category).data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'errors': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = ProductSerializers(product, many=False).data
        return Response(data=data_dict)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category = request.data.get('category')
        product.category_id = request.data.get('category_id')
        return Response(data=ProductSerializers(product).data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'errors': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = ReviewSerializers(review, many=False).data
        return Response(data=data_dict)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')
        return Response(data=ReviewSerializers(review).data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_reviews_api_view(request):
    product_review = Product.objects.all()
    avarage_stars = Review.objects.aggregate(avgarage_stars=Avg('stars'))
    data_dict = ProductReviewSerializers(product_review, many=True).data
    return Response(data=[data_dict, avarage_stars])
