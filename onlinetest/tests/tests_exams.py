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





class test_question(TestCase):

    def setUp(Self):
        ques_obj1 = question.objects.create( question_id='00001',
                                             question="What is the capital of India ?",
                                             option1="Delhi",
                                             option2="Bengaluru",
                                             option3="Mumbai",
                                             option4="Chennai",
                                             answer="1",
                                             date=datetime.now(tz=timezone.utc))

        ques_obj1 = question.objects.create( question_id='00002',
                                             question="National Animal of India ?",
                                             option1="Lion",
                                             option2="King cobra",
                                             option3="Tiger",
                                             option4="Asian Elephant",
                                             answer="3",
                                             date=datetime.now(tz=timezone.utc))
                                                

    def test_testDetails_question(self):
        q1 = question.objects.get(question_id='00001')
        q2 = question.objects.get(question_id='00002')

        self.assertEqual(str(q1), "What is the capital of India ?")
        self.assertEqual(str(q2), "National Animal of India ?")

    def test_testDetails_options(self):
        q1 = question.objects.get(question_id='00001')
        q2 = question.objects.get(question_id='00002')

        self.assertEqual(q1.option1, "Delhi")
        self.assertEqual(q1.option2, "Bengaluru")
        self.assertEqual(q1.option3, "Mumbai")
        self.assertEqual(q1.option4, "Chennai")

        self.assertEqual(q2.option1, "Lion")
        self.assertEqual(q2.option2, "King cobra")
        self.assertEqual(q2.option3, "Tiger")
        self.assertEqual(q2.option4, "Asian Elephant")

    def test_testDetails_answer(self):
        q1 = question.objects.get(question_id='00001')
        q2 = question.objects.get(question_id='00002')

        self.assertEqual(q1.answer, "1")
        self.assertEqual(q2.answer, "3")