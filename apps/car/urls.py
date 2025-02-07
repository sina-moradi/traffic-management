from django.urls import path

from .api.v1 import ColorFullCarListAPIView, OwnerCreateAPIView, CarCreateAPIView, OwnerAgeFilterListAPIView, \
    HeavyCarListAPIView, PositionCarAPIView, CarTollsAPIView , OwnerInfoListAPIView


urlpatterns = [
    path('colorfull/', ColorFullCarListAPIView.as_view()),
    path('owner/', OwnerCreateAPIView.as_view()),
    path('create/', CarCreateAPIView.as_view()),
    path('owner/age70/', OwnerAgeFilterListAPIView.as_view()),
    path('heavy_car_violation/', HeavyCarListAPIView.as_view()),
    path('owner/info/', OwnerInfoListAPIView.as_view()),
    path('positioning/', PositionCarAPIView.as_view()),
    path('tolls/<int:pk>/', CarTollsAPIView.as_view()),
]
