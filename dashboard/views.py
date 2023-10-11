from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from item.models import Item
from core.models import Profile


@login_required
def index(request):
    # Get the user and profile object.
    user = User.objects.get(username = request.user.username)
    profile = Profile.objects.get(user = user)
    
    items = Item.objects.filter(created_by = request.user)
    
    return render(request, 'dashboard/index.html', {
        'title': 'Dashboard',
        'items': items,
        'profile': profile,
    })
