from django.test import TestCase
from conversation.forms import ConversationMessageForm

class ConversationViewTestCase(TestCase):
    def test_new_conversation_form_valid(self):
        form = ConversationMessageForm(data={
            'content': 'This is a message',
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())