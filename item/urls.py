from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.view_items, name='view_items'),
    path('new/', views.new, name='new'),
    path('detail/<int:primary_key>/', views.detail, name='detail'),
    path('<int:primary_key>/edit/', views.edit, name='edit'),
    path('<int:primary_key>/delete/', views.delete, name='delete'),
]