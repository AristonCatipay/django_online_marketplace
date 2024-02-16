from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from item.models import Item
from .models import Metadata
from .forms import MessageForm

@login_required()
def inbox(request):
    # Get all the conversations connected to the item where the user is a member.
    metadata = Metadata.objects.filter(members__in=[request.user.id])

    return render(request, 'messenger/inbox.html', {
        'title': 'Inbox',
        'metadata': metadata,
    })

@login_required()
def add_message_or_redirect_to_messages(request, item_primary_key):
    item = Item.objects.get(pk=item_primary_key)
    reciever = item.created_by

    # If you are the owner then you should not be able to visit this page.
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # Get the metadata(conversation) that has the item and the current the user is a member.
    # If there is a metadata(conversation) already the current user will be redirected to that conversation.
    # If not then we will create one.
    metadata = Metadata.objects.filter(item=item).filter(members__in=[request.user.id])
    if metadata.exists():
        return redirect('messenger:messages', metadata_primary_key=metadata.first().id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Create the metadata
            metadata = Metadata.objects.create(item=item)
            metadata.members.add(request.user)
            metadata.members.add(item.created_by)
            metadata.save()

            # Save the message
            message = form.save(commit=False)
            message.metadata = metadata
            message.created_by = request.user
            message.save()

            return redirect('messenger:messages', metadata_primary_key=metadata.pk)
    else:
        form = MessageForm()

    return render(request, 'messenger/messages.html', {
        'title': 'Send Message',
        'form': form, 
        'reciever': reciever,
    })

@login_required()
def messages(request, metadata_primary_key):
    metadata = Metadata.objects.filter(members__in=[request.user.id]).get(pk=metadata_primary_key)
    reciever = metadata.members.exclude(id=request.user.id).first()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Save the message
            message = form.save(commit=False)
            message.metadata = metadata
            message.created_by = request.user
            message.save()

            metadata.save()
            return redirect('messenger:messages', metadata_primary_key=metadata_primary_key)
    else:
        form = MessageForm()

    return render(request, 'messenger/messages.html', {
        'title': 'Send Message',
        'metadata': metadata,
        'reciever': reciever,
        'form': form,
    })
