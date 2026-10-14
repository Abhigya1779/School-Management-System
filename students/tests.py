from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
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

    def test_update_student(self):
        self.student.name = "Jane Doe"
        self.student.save()
        self.student.refresh_from_db()
        self.assertEqual(
            self.student.name, "Jane Doe"
        )

    class StudentPageTest(TestCase):
        def test_student_list_page(self):
            response = self.client.get(
                reverse("student_list")
            )

            self.assertEqual(
                response.status_code, 200
            )

    class AuthenticationTest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(
                username="testuser",
                password="testpassword"
            )

        def test_anonymous_user_redirected_to_login(self):
            response = self.client.get(
                reverse("profile")
            )
            self.assertEqual(
                response.status_code, 302
            )

        def test_logged_in_user_can_access_profile(self):
            self.client.force_login(self.user)
            response = self.client.get(
                reverse("profile")
            )

            self.assertEqual(
                response.status_code, 200   
            )