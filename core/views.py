from django.shortcuts import render, redirect
from item.models import Category, Item
from . forms import SignupForm

def index(request):
    # Retrieving only 6 items that is marked as unsold.
    items = Item.objects.filter(is_sold = False)[0:6]
    # Retrieving all the categories.
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    # If the user makes a POST request.
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
        'title': 'Sign up',
    })
