from django.test import TestCase
import datetime
from onlinetest.models import studentMark, studentProfile
# Create your tests here.


class testStudentModels(TestCase):
	def setUp(self):
		studentProfile.objects.create(name = "Student 1", email = "fake-email@gmail.com",
			password = "pwd1", rollno = "number 1", client = "client1", date = datetime.datetime.now())
		studentMark.objects.create( studentid = "st1", ques_paper_id = "paper1", marks = "12",
			name = "Student 1", email = "fake-email@gmail.com", testtitle = "test1",
			client = "client1", date = datetime.datetime.now(), )

	def testCreatedObjects(self):
		self.assertEqual(studentMark.objects.get(studentid="std1").client, "client1")
		self.assertEqual(studentProfile.objects.get(name="Student 1").testtitle, "test1")