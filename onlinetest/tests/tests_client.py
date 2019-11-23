from django.test import TestCase
from onlinetest.models import clientsTable 
from datetime import datetime

class clientsTableTest(TestCase):

    def setUp(Self):
        test_obj1 = clientsTable.objects.create(name='Vennela',
                                    email="vennela@gmail.com",
                                    contactNumber="",
                                    pwd="vennelapassword")
                                    #date=str(datetime.now))
        test_obj2 = clientsTable.objects.create(name='alks',
                                    email="alka23@gmail.com",
                                    contactNumber="8543242444",
                                    pwd="alkapassword")
                                    #date=str(datetime.now))
        test_obj1.save()
        test_obj2.save()

    def test_returns_email(self):
        bennelbaz = clientsTable.objects.get(name='Vennela')
        alks = clientsTable.objects.get(name='alks')

        self.assertEqual(str(bennelbaz), "vennela@gmail.com")
        self.assertEqual(str(alks), "alka23@gmail.com")
