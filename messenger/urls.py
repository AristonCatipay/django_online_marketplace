from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('messages/<int:metadata_primary_key>/', views.messages, name='messages'),
    path('connect/<int:item_primary_key>/', views.add_message_or_redirect_to_messages, name='add_message_or_redirect_to_messages'),
]