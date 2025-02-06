from django.urls import path

from .api.v1 import ColorFullCarListAPIView


urlpatterns = [
    path('colorfull_cars/', ColorFullCarListAPIView.as_view()),
]