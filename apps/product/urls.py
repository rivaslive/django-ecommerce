from django.urls import path

from apps.product import views

urlpatterns = [
    path('', views.all_products),
]
