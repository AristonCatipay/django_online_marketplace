from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from . models import Profile

def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    return render(request, 'profile/index.html', {
        'title': 'Profile',
        'profile': profile,
        'user': user,
    })

def edit(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    return render(request, 'profile/edit.html', {
        'title': 'Edit Profile',
        'profile': profile,
        'user': user,
    })