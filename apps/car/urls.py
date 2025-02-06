from django.urls import path

from .api.v1 import ColorFullCarListAPIView, OwnerCreateAPIView, CarCreateAPIView


urlpatterns = [
    path('colorfull_cars/', ColorFullCarListAPIView.as_view()),
    path('owner/', OwnerCreateAPIView.as_view()),
    path('car_create/', CarCreateAPIView.as_view()),
]