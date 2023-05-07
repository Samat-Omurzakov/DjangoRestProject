from rest_framework import serializers
from product.models import Category, Product, Review


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'id name'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class ProductReviewSerializers(serializers.ModelSerializer):
    product_review = ReviewSerializers(many=True)

    class Meta:
        model = Product
        fields = 'title product_review'.split()
