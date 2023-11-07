from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from user_profile.models import Profile
from . models import Conversation
from . forms import ConversationMessageForm

@login_required
def new_conversation(request, primary_key):
    # Get the user and profile object.
    user = User.objects.get(username = request.user.username)
    profile = Profile.objects.get(user = user)

    item = get_object_or_404(Item, id=primary_key)

    # If you are the owner then you should not be able to visit this page.
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # Get all the conversations connected to the item where the user is a member.
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    # If there is a conversation already you will be redirected to that conversation.
    # If not then we will create one.

    if conversations:
        return redirect('conversation:conversation_detail', conversation_primary_key=conversations.first().id)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)    

        if form.is_valid():
            # Add the user to the members of the conversation(members list).
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            # Add the conversation message.
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', primary_key=primary_key)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/form.html', {
        'title': 'New Conversation',
        'form': form, 
        'profile': profile
    })


@login_required
def inbox(request):
    # Get all the conversations connected to the item where the user is a member.
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'title': 'Inbox',
        'conversations': conversations,
    })

@login_required
def conversation_detail(request, conversation_primary_key):
    # Get the user and profile object.
    user = User.objects.get(username = request.user.username)
    profile = Profile.objects.get(user = user)

    # Get all the conversations connected to the item where the user is a member.
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(id=conversation_primary_key)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:conversation_detail', conversation_primary_key=conversation_primary_key)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'title': 'Conversation Detail',
        'conversation': conversation,
        'form': form,
        'profile': profile,
    })
