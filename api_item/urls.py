from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_items),
    path('detail/<int:item_primary_key>/', views.read_item_detail)
]