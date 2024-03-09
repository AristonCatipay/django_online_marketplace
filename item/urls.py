from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.view_items, name='view_items'),
    path('detail/<int:item_primary_key>/', views.view_item_detail, name='view_item_detail'),
    path('create/', views.create_item, name='create_item'),
    path('<int:primary_key>/edit/', views.edit, name='edit'),
    path('<int:primary_key>/delete/', views.delete, name='delete'),
]