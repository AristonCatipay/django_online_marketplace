from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_current_user_items),
    path('update/<int:item_primary_key>/', views.update_current_user_item)
]