from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('users/', views.read_user),
    path('logout/', views.logout),
    path('items-categories/read/', views.read_items_and_categories),
]