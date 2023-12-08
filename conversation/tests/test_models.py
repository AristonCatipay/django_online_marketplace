from django.test import TestCase
from django.contrib.auth.models import User
from conversation.models import Conversation, ConversationMessage
from item.models import Item, Category

class ConversationModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.category = Category.objects.create(
            name = 'test category'
        )
        self.item = Item.objects.create(
            category = self.category,
            created_by = self.user1,
            name = 'test item',
            description = 'test description',
            price = 100,
            image = 'default_profile_image.jpg',
        )

    def test_conversation_creation(self):
        conversation = Conversation.objects.create(item=self.item)
        conversation.members.add(self.user1)
        conversation.members.add(self.user2)

        self.assertEqual(conversation.item, self.item)
        self.assertIn(self.user1, conversation.members.all())
        self.assertIn(self.user2, conversation.members.all())
    
    def tearDown(self):
        self.item.delete()
        self.category.delete()
        self.user2.delete()
        self.user1.delete()


