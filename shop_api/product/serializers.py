from rest_framework import serializers
from .models import Category, Product, Review
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=1, max_length=100,allow_blank=False)
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1, max_length=100,allow_blank=False)
    description = serializers.CharField(min_length=5, max_length=1000, allow_blank=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(validators=[MinLengthValidator(3)], allow_blank=False)
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