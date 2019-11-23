from django.test import TestCase
from django.utils import timezone
from onlinetest.models import clientsTable
from datetime import datetime

class test_clientsTableTest(TestCase):

    def setUp(Self):
        test_obj1 = clientsTable.objects.create(name='vennela',
                                    			email="vennela@gmail.com",
                                    			contactNumber="9999988888",
                                    			pwd="vennelapassword",
                                    			date=datetime.now(tz=timezone.utc))
        test_obj2 = clientsTable.objects.create(name='alks',
                                    			email="alks23@gmail.com",
                                    			contactNumber="8543242444",
                                    			pwd="alkspassword",
                                    			date=datetime.now(tz=timezone.utc))


    def test_clientsTableTest_name(self):
    	vennela = clientsTable.objects.get(name='vennela')
    	alks = clientsTable.objects.get(name='alks')

    	self.assertEqual(vennela.name, "vennela")
    	self.assertEqual(alks.name, "alks")

    def test_clientsTableTest_email(self):
        vennela = clientsTable.objects.get(name='vennela')
        alks = clientsTable.objects.get(name='alks')

        self.assertEqual(str(vennela), "vennela@gmail.com")
        self.assertEqual(str(alks), "alks23@gmail.com")


    def test_clientsTableTest_contactNumber(self):
    	vennela = clientsTable.objects.get(name='vennela')
    	alks = clientsTable.objects.get(name='alks')

    	self.assertEqual(vennela.contactNumber, "9999988888")
    	self.assertEqual(alks.contactNumber, "8543242444")

    def test_clientsTableTest_pwd(self):
    	vennela = clientsTable.objects.get(name='vennela')
    	alks = clientsTable.objects.get(name='alks')

    	self.assertEqual(vennela.pwd, "vennelapassword")
    	self.assertEqual(alks.pwd, "alkspassword")