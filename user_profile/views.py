from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        location = request.POST['location']

        if request.FILES.get('image') == None:
            # If the user didn't upload their own image
            # Use the default profile image.
            image = profile.image

            # Update profile model
            profile.image = image
            profile.location = location
            profile.save()

            # Update user model
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')

            # Update profile model
            profile.image = image
            profile.location = location
            profile.save()

            # Update user model
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
        
        return redirect('profile:edit')

    return render(request, 'profile/edit.html', {
        'title': 'Edit Profile',
        'profile': profile,
        'user': user,
    })