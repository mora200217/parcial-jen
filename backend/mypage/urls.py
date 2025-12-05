# mypage/urls.py
from django.urls import path
from .views import FoodListCreateView  # revisa que el import sea correcto

urlpatterns = [
    path('api/foods/', FoodListCreateView.as_view(), name='food-list-create'),
]
