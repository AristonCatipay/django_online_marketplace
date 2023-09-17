from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from . models import Conversation
from . forms import ConversationMessageForm

@login_required
def new_conversation(request, primary_key):
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

    return render(request, 'conversation/new.html', {
        'form': form, 
        'title': 'New Conversation',
    })


@login_required
def inbox(request):
    # Get all the conversations connected to the item where the user is a member.
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'title': 'Inbox',
    })

@login_required
def conversation_detail(request, conversation_primary_key):
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
        'conversation': conversation,
        'form': form,
        'title': 'Conversation Detail',
    })
