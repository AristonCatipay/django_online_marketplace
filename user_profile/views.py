from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from address.models import Region, Province, City_Municipality, Barangay

@login_required
def index(request):
    return render(request, 'profile/index.html', {
        'title': 'Profile',
    })

@login_required
def update_profile(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            gender = request.POST['gender']
            image = request.FILES.get('image')

            if image:
                request.user.profile.image = image
            request.user.profile.gender = gender
            request.user.profile.save()

            # Update user model
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.username = username
            request.user.email = email
            request.user.save()

            messages.success(request, "Profile updated successfully! Your changes have been saved.")
            return redirect('profile:update_profile')
        except Exception as e:
            messages.error(request, f"Failed to update profile. {e}")
    
    return render(request, 'profile/update_profile.html', {
        'title': 'Edit Profile',
    })

@login_required
def update_address(request):
    regions = Region.objects.all()

    if request.method == 'POST':
        try:
            region = request.POST['region']
            province = request.POST['province']
            city_municipality = request.POST['city_municipality']
            barangay = request.POST['barangay']
            location = request.POST['location']

            region = get_object_or_404(Region, pk=region)
            province = get_object_or_404(Province, pk=province)
            city_municipality = get_object_or_404(City_Municipality, pk=city_municipality)
            barangay = get_object_or_404(Barangay, pk=barangay)
            request.user.profile.region = region
            request.user.profile.province = province
            request.user.profile.city_municipality = city_municipality
            request.user.profile.barangay = barangay
            request.user.profile.location = location
            request.user.profile.save()

            messages.success(request, "User address updated successfully! Your changes have been saved.")
            return redirect('profile:update_address')
        except Exception as e:
            messages.error(request, f"Failed to update address. {e}")
    
    return render(request, 'profile/update_address.html', {
        'title': 'Edit User Address',
        'regions': regions,
    })

@login_required
def load_province(request):
    region = request.GET.get('region')
    provinces = Province.objects.filter(region=region)
    return render(request, 'profile/load/province_options.html', {
        'provinces': provinces,
    })

@login_required
def load_city_municipality(request):
    province = request.GET.get('province')
    city_municipalities = City_Municipality.objects.filter(province=province)
    return render(request, 'profile/load/city_municipality_options.html', {
        'city_municipalities': city_municipalities,
    })

@login_required
def load_barangay(request):
    city_municipality = request.GET.get('city_municipality')
    barangays = Barangay.objects.filter(city_municipality=city_municipality)
    return render(request, 'profile/load/barangay_options.html', {
        'barangays': barangays,
    })

@login_required
def update_password(request):
    if request.method == 'POST':
        try:
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            confirm_new_password = request.POST['confirm_new_password']
            
            if request.user.check_password(old_password):
                if new_password == confirm_new_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    messages.success(request, 'Password updated successfully!')
                    return redirect('core:signin')
                else:
                    messages.error(request, 'Failed to update password. New password does not match.')
                    return redirect('profile:update_password')
            else:
                messages.error(request, 'Failed to update password. Old password does not match.')
                return redirect('profile:update_password')
        except Exception as e:
            messages.error(request, f"Failed to change password. {e}")
    
    return render(request, 'profile/update_password.html', {
        'title': 'Change Password',
    })