from django.test import TestCase

from students.models import Student

# Create your tests here.

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            age=20,
            address="kathmandu",
        )

    def test_student_is_created(self):
        self.assertEqual(
            Student.objects.count(), 1
        )

    def test_student_name(self):
        self.assertEqual(
            self.student.name, "John Doe"
        )

