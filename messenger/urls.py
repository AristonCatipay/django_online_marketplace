from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
]