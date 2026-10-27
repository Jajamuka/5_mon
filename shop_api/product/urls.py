from django.urls import path
from .views import (
    category_list_api_view,
    category_detail_api_view,
    product_list_api_view,
    product_detail_api_view,
    review_list_api_view,
    review_detail_api_view,
)

urlpatterns = [
    path('categories/', category_list_api_view),
    path('categories/<int:id>/', category_detail_api_view),
    path('products/', product_list_api_view),
    path('products/<int:id>/', product_detail_api_view),
    path('reviews/', review_list_api_view),
    path('reviews/<int:id>/', review_detail_api_view),
]