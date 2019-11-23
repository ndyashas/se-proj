from django.test import TestCase
from django.utils import timezone
from onlinetest.models import testDetails, question
from datetime import datetime

class test_testDetails(TestCase):

    def setUp(Self):
        test_obj1 = testDetails.objects.create( test_id='2019112206537',
                                    			client_id="vennelaclient",
                                    			testtitle="Mathematics",
                                    			testduration="15",
                                    			date=datetime.now(tz=timezone.utc),
                                    			re_answers="AAAABBBBCCCCDDDDEEEE")
        test_obj2 = testDetails.objects.create( test_id='2019112312595',
                                    			client_id="alksclient",
                                    			testtitle="English",
                                    			testduration="20",
                                    			date=datetime.now(tz=timezone.utc),
                                    			re_answers="AAAABBBBCCCCDDDDEEEE")


    def test_testDetails_test_id(self):
    	t1 = testDetails.objects.get(test_id='2019112206537')
    	t2 = testDetails.objects.get(test_id='2019112312595')

    	self.assertEqual(str(t1), "2019112206537")
    	self.assertEqual(str(t2), "2019112312595")

    def test_testDetails_client_id(self):
    	t1 = testDetails.objects.get(test_id='2019112206537')
    	t2 = testDetails.objects.get(test_id='2019112312595')

    	self.assertEqual(t1.client_id, "vennelaclient")
    	self.assertEqual(t2.client_id, "alksclient")

    def test_testDetails_testtitle(self):
    	t1 = testDetails.objects.get(test_id='2019112206537')
    	t2 = testDetails.objects.get(test_id='2019112312595')

    	self.assertEqual(t1.testtitle, "Mathematics")
    	self.assertEqual(t2.testtitle, "English")

    def test_testDetails_testduration(self):
    	t1 = testDetails.objects.get(test_id='2019112206537')
    	t2 = testDetails.objects.get(test_id='2019112312595')

    	self.assertEqual(t1.testduration, "15")
    	self.assertEqual(t2.testduration, "20")

    def test_testDetails_re_answers(self):
    	t1 = testDetails.objects.get(test_id='2019112206537')
    	t2 = testDetails.objects.get(test_id='2019112312595')

    	self.assertEqual(t1.re_answers, "AAAABBBBCCCCDDDDEEEE")
    	self.assertEqual(t2.re_answers, "AAAABBBBCCCCDDDDEEEE")
