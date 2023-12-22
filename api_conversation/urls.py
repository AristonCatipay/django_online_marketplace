from django.urls import path
from . import views

urlpatterns = [
    path('inbox/read/', views.read_inbox),
    path('messages/<int:conversation_primary_key>/', views.read_conversation_messages),
]