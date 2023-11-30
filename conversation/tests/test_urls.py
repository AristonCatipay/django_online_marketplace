from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from conversation.models import Conversation, ConversationMessage
from conversation.views import inbox, new_conversation, conversation_detail
from item.models import Category, Item

class ConversationUrlTestCase(TestCase):
    def setUp(self):
        self.user = self.create_test_user()
        self.category = self.create_test_category()
        self.item = self.create_test_item()
        self.conversation = self.create_test_conversation()
        self.conversation.members.add(self.user)
        self.conversation_message = self.create_test_conversation_message()

    def tearDown(self):
        self.user.delete()
        self.category.delete()
        self.item.delete()
        self.conversation.delete()
        self.conversation_message.delete()

    def create_test_user(self):
        return User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username = 'testuser',
            email = 'emailtest',
            password = '12345'
        )

    def create_test_category(self):
        return Category.objects.create(name = 'test category')
    
    def create_test_item(self):
        return Item.objects.create(
            category = self.category,
            created_by = self.user,
            name = 'test item',
            description = 'test description',
            price = 100,
            image = 'default_profile_image.jpg'
        )

    def create_test_conversation(self):
        return Conversation.objects.create(
            item = self.item,
        )
    
    def create_test_conversation_message(self):
        return ConversationMessage.objects.create(
            conversation = self.conversation,
            content = 'Test content message',
            created_by = self.user,
        )
    
    def test_inbox_url(self):
        url = reverse('conversation:inbox')
        self.assertEquals(resolve(url).func, inbox)

    def test_new_conversation_url(self):
        url = reverse('conversation:new', args=[self.item.pk])
        self.assertEquals(resolve(url).func, new_conversation)

    def test_conversation_detail_url(self):
        url = reverse('conversation:conversation_detail', args=[self.conversation.pk])
        self.assertEquals(resolve(url).func, conversation_detail)