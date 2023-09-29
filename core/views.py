from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from item.models import Category, Item
from . forms import SignupForm

def index(request):
    # Retrieving only 6 items that is marked as unsold.
    items = Item.objects.filter(is_sold = False)[0:6]
    # Retrieving all the categories.
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'title': 'Welcome',
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html', {
        'title': 'Contact',
    })

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already taken.')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This username is already taken.')
                return redirect('core:signup')
            else:
                # Create the user.
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # Log the user in using the said credentials.
                user_credentials = auth.authenticate(username=username, password=password)
                auth.login(request, user_credentials)
                
                return redirect('core:index')

        else:
            messages.info(request, 'Password don\'t match.')
            return redirect('core:signup')
    else:
        return render(request, 'core/signup.html', {
            'title': 'Sign up',
        }) 
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            auth.login(request, user)
            return redirect('core:index')
        else:
            # No backend authenticated the credentials
            messages.info(request, 'Invalid credentials.')
            return redirect('core:signin')
    else:
        return render(request, 'core/signin.html', {
            'title': 'Login',
        })
    

def logout(request):
    auth.logout(request)
    return redirect('core:signin')