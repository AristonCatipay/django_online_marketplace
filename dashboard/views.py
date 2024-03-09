from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from item.models import Item


@login_required
def view_user_items(request):
    items = Item.objects.filter(created_by = request.user)
    
    return render(request, 'dashboard/view_user_items.html', {
        'title': 'Dashboard',
        'items': items,
    })
