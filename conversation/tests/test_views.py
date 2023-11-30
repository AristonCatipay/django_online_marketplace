from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from conversation.models import Conversation, ConversationMessage
from user_profile.models import Profile
from item.models import Item, Category

class ConversationViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.profile = Profile.objects.create(
            user = self.user,
            image = 'media/default_profile_image.jpg',
            location = 'Some Location',
        )

        self.category = Category.objects.create(
            name = 'test category'
        )
        
        self.item = Item.objects.create(
            category = self.category,
            created_by = self.user,
            name = 'test item',
            description = 'test description',
            price = 100,
            image = 'default_profile_image.jpg',
        )

        self.conversation = Conversation.objects.create(
            item = self.item,
        )
        self.conversation.members.add(self.user)

        self.conversation_message = ConversationMessage.objects.create(
            conversation = self.conversation,
            content = 'Test content message',
            created_by = self.user,
        )

    def test_inbox_view(self):
        self.client.force_login(self.user)
        url = reverse('conversation:inbox')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation/inbox.html')

    def test_new_conversation_view(self):
        self.client.force_login(self.user)
        url = reverse('conversation:new', kwargs={'primary_key': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation/form.html')
    
    def tearDown(self):
        self.conversation_message.delete()
        self.conversation.delete()
        self.item.delete()
        self.category.delete()
        self.profile.delete()
        self.user.delete()
