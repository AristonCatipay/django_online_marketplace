from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'profile/index.html', {
        'title': 'Profile',
    })

@login_required
def edit(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            location = request.POST['location']
            image = request.FILES.get('image')

            if image:
                request.user.profile.image = image
            request.user.profile.location = location
            request.user.profile.save()

            # Update user model
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.username = username
            request.user.email = email
            request.user.save()

            messages.success(request, "Profile updated successfully! Your changes have been saved.")
            return redirect('profile:edit')
        except Exception as e:
            messages.error(request, f"Failed to update profile. {e}")
    
    return render(request, 'profile/edit.html', {
        'title': 'Edit Profile',
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']
        
        if new_password == confirm_new_password:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Password updated successfully!')
            return redirect('core:signin')
        else:
            messages.error(request, 'Failed to update password. New password does not match.')
            return redirect('profile:change_password')
    
    return render(request, 'profile/change_password.html', {
        'title': 'Change Password',
    })