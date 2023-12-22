from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_current_user_profile),
]