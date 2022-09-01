from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Preorder

class MenuTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="uncommon")
        testuser1.save()

        test_thing = Preorder.objects.create(client=testuser1, item="MacBook Pro", prime=True,
                                         price=1200)
        test_thing.save()


    def test_things_model(self):
        preorder_1= Preorder.objects.get(id=1)
        actual_client = str(preorder_1.client)
        actual_item= str(preorder_1.item)
        actual_price = str(preorder_1.price)
        actual_prime = str(preorder_1.prime)
        self.assertEqual(actual_client, "testuser1")
        self.assertEqual(actual_item, "MacBook Pro")
        self.assertEqual(actual_price, '1200')
        self.assertEqual(actual_prime, 'True')