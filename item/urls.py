from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:primary_key>/', views.detail, name='detail'),
    path('<int:primary_key>/delete/', views.delete, name='delete'),
    path('<int:primary_key>/edit/', views.edit, name='edit'),
]