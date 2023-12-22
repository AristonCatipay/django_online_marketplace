from django.urls import path
from . import views

urlpatterns = [
    path('user/read/', views.read_current_user_items),
]