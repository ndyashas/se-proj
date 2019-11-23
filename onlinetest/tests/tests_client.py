from django.test import TestCase
from onlinetest.models import clientsTable 
from datetime import datetime

class clientsTableTest(TestCase):

    def setUp(Self):
        clientsTable.objects.create(name='Vennela',
                                    email="vennela@gmail.com",
                                    contactNumber="",
                                    pwd="vennelapassword",
                                    date=datetime.datetime.now)
        clientsTable.objects.create(name='alks',
                                    email="alka23@gmail.com",
                                    contactNumber="8543242444",
                                    pwd="alkapassword",
                                    date=datetime.datetime.now)

    def check_returns_email(self):
        bennelbaz = clientsTable.objects.get(name='Bennelbaz')
        alks = clientsTable.objects.get(name='alks')

        self.assertEqual(str(bennelbaz), "b@b.com")
        self.assertEqual(str(alks), "a@a.com")
