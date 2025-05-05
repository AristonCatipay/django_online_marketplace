from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.view_user_items, name='view_user_items'),
]