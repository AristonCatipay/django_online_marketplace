from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_inbox),
    path('create/<int:item_primary_key>/', views.create_new_conversation),
    path('messages/<int:conversation_primary_key>/', views.read_conversation_messages),
    path('messages/create/<int:conversation_primary_key>/', views.create_message),
]