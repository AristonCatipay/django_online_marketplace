from django.shortcuts import render
from item.models import Category, Item



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