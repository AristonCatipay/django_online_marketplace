from django.shortcuts import render, get_object_or_404
from . models import Item

def detail(request, primary_key):
    # Using the primary key we can get the specific item we want to display.
    item = get_object_or_404(Item, id = primary_key)

    # We can also get the related items or items that are in the same category.
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=primary_key)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items' : related_items
    })
