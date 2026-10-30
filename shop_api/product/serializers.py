from rest_framework import serializers
from .models import Category, Product, Review
from django.core.validators import MinValueValidator, MaxValueValidator


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    stars = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        model = Review
        fields = '__all__'

class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'reviews', 'rating']