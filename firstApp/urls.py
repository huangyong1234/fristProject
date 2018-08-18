from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('request/', views.use_simple_requests),
    path('request2/', views.use_simple_requests),
]