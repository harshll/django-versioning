from django.urls import path

from .views import TestView,StudentView


urlpatterns = [
    path('verson/',TestView.as_view()),
    path('students/<int:pk>',StudentView.as_view())
]
