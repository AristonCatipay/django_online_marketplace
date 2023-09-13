from django.shortcuts import render, get_object_or_404
from . models import Item

def detail(request, primary_key):
    item = get_object_or_404(Item, id = primary_key)

    return render(request, 'item/detail.html', {
        'item': item
    })
