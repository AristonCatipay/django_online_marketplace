from django.urls import path
from . import views

urlpatterns = [
    path('inbox/read/', views.read_inbox),
]