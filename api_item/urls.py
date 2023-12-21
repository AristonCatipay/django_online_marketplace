from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_items),
    path('detail/<int:item_primary_key>/', views.read_item_detail),
    path('create/', views.create_item),
    path('update/<int:item_primary_key>/', views.update_item),
]