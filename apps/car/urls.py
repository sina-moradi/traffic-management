from django.urls import path

from .api.v1 import ColorFullCarListAPIView, OwnerCreateAPIView, CarCreateAPIView, OwnerAgeFilterListAPIView, \
    HeavyCarListAPIView


urlpatterns = [
    path('colorfull_cars/', ColorFullCarListAPIView.as_view()),
    path('owner/', OwnerCreateAPIView.as_view()),
    path('car_create/', CarCreateAPIView.as_view()),
    path('owner_age70/', OwnerAgeFilterListAPIView.as_view()),
    path('heavy_car_violation/', HeavyCarListAPIView.as_view()),
]