from django.urls import path
from . import views

urlpatterns = [
    path('items-categories/read/', views.read_items_and_categories),
]