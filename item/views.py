from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from . models import Item
from . forms import NewItemForm

def detail(request, primary_key):
    # Using the primary key we can get the specific item we want to display.
    item = get_object_or_404(Item, id = primary_key)

    # We can also get the related items or items that are in the same category.
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=primary_key)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items' : related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # Before we commit we need to add the user that made the request to the query.
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', primary_key = item.id)
    else: 
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })

@login_required
def delete(request, primary_key):
    item = get_object_or_404(Item, id = primary_key, created_by = request.user)
    item.delete()

    return redirect('dashboard:index')