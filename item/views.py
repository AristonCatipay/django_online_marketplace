from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages

from PIL import Image

from . models import Item, Category
from user_profile.models import Profile
from . forms import NewItemForm, EditItemForm

@login_required
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items, 
        'query': query,
        'title': 'Items',
        'categories': categories,
        'category_id': int(category_id),
    })

@login_required
def detail(request, primary_key):
    # Using the primary key we can get the specific item we want to display.
    item = get_object_or_404(Item, id = primary_key)

    # Get the profile picture of the user selling.
    seller = Profile.objects.get(user_id = item.created_by )

    # We can also get the related items or items that are in the same category.
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=primary_key)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items' : related_items,
        'seller': seller,
    })

def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                item = form.save(commit=False)
                image = Image.open(form.cleaned_data['image'])
                
                # Resize the image while maintaining aspect ratio
                resized_image = resize_image(image, 600)
                
                # Save the resized image to a temporary in-memory file
                from io import BytesIO
                temp_image = BytesIO()
                resized_image.save(temp_image, format='JPEG')  # Change the format if needed
                
                # Save the image to the item instance and the rest of the form
                item.image.save(f'{item.name}_resized.jpg', temp_image, save=False)
                item.created_by = request.user
                item.save()

                return redirect('item:detail', primary_key=item.id)
            except Exception as e:
                print(f"Error processing image: {e}")
                messages.error(request, "There was an issue processing the image. Please ensure it's a valid image file and try again.")
                return redirect('item:new')
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'title': 'Sell Item',
        'form': form,
    })

@login_required
def edit(request, primary_key):
    item = get_object_or_404(Item, id = primary_key, created_by = request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', primary_key = item.id)
    else: 
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'title': 'Edit Item',
        'form': form,
    })

@login_required
def delete(request, primary_key):
    item = get_object_or_404(Item, id = primary_key, created_by = request.user)
    item.delete()

    return redirect('dashboard:index')