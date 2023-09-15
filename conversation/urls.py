from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:conversation_primary_key>/', views.conversation_detail, name='conversation_detail'),
    path('new/<int:primary_key>/', views.new_conversation, name='new'),
]