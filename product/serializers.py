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


class ProductValidateSerializers(serializers.Serializer):
    title = serializers.CharField(min_length=1)
    description = serializers.CharField(min_length=1, required=False)
    price = serializers.FloatField(min_value=0)
    category_id = serializers.IntegerField(min_value=1)


class CategoryValidateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class ReviewValidateSerializers(serializers.Serializer):
    text = serializers.CharField(min_length=1)
    product_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1)
