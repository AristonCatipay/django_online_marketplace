from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('items-categories/read/', views.read_items_and_categories),
]