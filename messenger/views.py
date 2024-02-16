from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Metadata
from .forms import MessageForm

@login_required()
def inbox(request):
    # Get all the conversations connected to the item where the user is a member.
    metadata = Metadata.objects.filter(members__in=[request.user.id])

    return render(request, 'messenger/inbox.html', {
        'title': 'Messenger',
        'metadata': metadata,
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
