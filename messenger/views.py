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
