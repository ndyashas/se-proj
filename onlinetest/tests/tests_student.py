from django.test import TestCase
import datetime
from django.utils import timezone
from onlinetest.models import studentMark, studentProfile

class testStudentModels(TestCase):
	def setUp(self):
		studentProfile.objects.create(name="Student 1",
				email = "fake-email@gmail.com",
				password = "pwd1",
				rollno = "number 1",
				client = "client1",
				date = datetime.datetime.now(tz=timezone.utc))
		studentMark.objects.create(studentid = "st1",
				ques_paper_id = "paper1",
				marks = "12",
				name = "Student 1",
				email = "fake-email@gmail.com",
				testtitle = "test1",
				client = "client1",
				date = datetime.datetime.now(tz=timezone.utc),
				answers = "12344",
				comments = "comment1___comment2")

	def test_studentdetails(self):
		studentMark_obj = studentMark.objects.get(studentid="st1")
		studentProfile_obj = studentProfile.objects.get(name="Student 1") 
		self.assertEqual(studentMark_obj.client,"client1")
		self.assertEqual(studentProfile_obj.name,"Student 1")

	def test_clientdetails(self):
		studentMark_obj = studentMark.objects.get(name="Student 1")
		studentProfile_obj = studentProfile.objects.get(client="client1") 
		self.assertEqual(studentMark_obj.email,"fake-email@gmail.com")
		self.assertEqual(studentProfile_obj.client,"client1")

	def test_studentResponses(self):
		studentMark_obj = studentMark.objects.get(email="fake-email@gmail.com")
		studentProfile_obj = studentProfile.objects.get(rollno="number 1") 
		self.assertEqual(studentMark_obj.studentid,"st1")
		self.assertEqual(studentProfile_obj.password,"pwd1")