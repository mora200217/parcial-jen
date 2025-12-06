from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path("items/", ItemList.as_view()),
    path("items/<str:pk>/", ItemDetail.as_view()),
]
