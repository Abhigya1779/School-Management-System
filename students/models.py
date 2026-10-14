from django.db import models

class AIConversation(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    subjects = models.ManyToManyField(Subject)
    document = models.FileField(upload_to="documents/",blank=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.age} {self.address} {self.course}"

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15)
    university = models.CharField(max_length=100)

    def __str__(self):
        return f"Profile of {self.student.name}"

# Import model
# from students.models import Student

# Get all students
# Student.objects.all()

# Store all students
# students = Student.objects.all()

# Print students
# print(students)

# Loop through students
# for student in students:
#     print(student)

# Print student details
# for student in students:
#     print(student.name)
#     print(student.email)
#     print(student.age)
#     print(student.address)

# Create a student
# Student.objects.create(
#     name="Sita",
#     email="sita@gmail.com",
#     age=22,
#     address="Pokhara"
# )

# Get student by ID
# Student.objects.get(id=2)

# Get student by age
# Student.objects.get(age=22)

# Store student in variable
# Ram = Student.objects.get(id=2)

# Print student
# print(Ram)

# Change student's age
# Ram.age = 25

# Save changes
# Ram.save()

# Get all students as dictionaries
# Student.objects.all().values()

# Store Sita in variable
# SitaD = Student.objects.get(age=22)

# Delete Sita
# SitaD.delete()

# Create another student
# Student.objects.create(
#     name="Sita",
#     email="sita@gmail.com",
#     age=23,
#     address="tinkune"
# )

# Get Sita
#Sita = Student.objects.get(age=23)

# Access student's address
#Sita.address

# Access student's email
#Sita.email

# Order by age - ascending
#Student.objects.all().order_by("age")

# Order by age - descending
#Student.objects.all().order_by("-age")

# Order by name
#Student.objects.all().order_by("name")

# Filter age greater than 18
#Student.objects.filter(age__gt=18)

# Filter age greater than 22
#Student.objects.filter(age__gt=22)

# Filter age less than 22
#Student.objects.filter(age__lt=22)

# Filter names using __in
#Student.objects.filter(name__in=["Krishna", "hari", "gopal"])

# Another __in example
#Student.objects.filter(name__in=["Sita", "hari", "gopal"])

# Exit Django shell
#exit()
   
# ```python
# # ==========================================
# # DJANGO ORM - ALL VALID QUERIES
# # ==========================================


# # ------------------------------------------
# # IMPORT MODELS
# # ------------------------------------------

# # Import Student model
# from students.models import Student

# # Import Course model
# from students.models import Course

# # Import Student, Course and StudentProfile
# from students.models import Student, Course, StudentProfile


# # ==========================================
# # STUDENT QUERIES
# # ==========================================

# # Get all students
# Student.objects.all()


# # Store all students
# students = Student.objects.all()


# # Print all students
# print(students)


# # Loop through students
# for student in students:
#     print(student)


# # Print student details
# for student in students:
#     print(student.name)
#     print(student.email)
#     print(student.age)
#     print(student.address)


# # Create a student
# Student.objects.create(
#     name="Sita",
#     email="sita@gmail.com",
#     age=22,
#     address="Pokhara"
# )


# # Get student by ID
# Student.objects.get(id=2)


# # Get student by age
# Student.objects.get(age=22)


# # Store student in variable
# Ram = Student.objects.get(id=2)


# # Print student
# print(Ram)


# # Print student's course
# print(Ram.course)


# # Change student's age
# Ram.age = 25


# # Save changes
# Ram.save()


# # Get all students as dictionaries
# Student.objects.all().values()


# # Store student in variable
# student = Student.objects.get(id=1)


# # Change student's name
# student.name = "Abhi"


# # Save changes
# student.save()


# # Create another student
# Student.objects.create(
#     name="Sita",
#     email="sita@gmail.com",
#     age=23,
#     address="tinkune"
# )


# # Get Sita
# Sita = Student.objects.get(age=23)


# # Access Sita's address
# Sita.address


# # Access Sita's email
# Sita.email


# # ==========================================
# # ORDERING
# # ==========================================

# # Order students by age - ascending
# Student.objects.all().order_by("age")


# # Order students by age - descending
# Student.objects.all().order_by("-age")


# # Order students by name
# Student.objects.all().order_by("name")


# # ==========================================
# # FILTERING
# # ==========================================

# # Age greater than 18
# Student.objects.filter(age__gt=18)


# # Age greater than 22
# Student.objects.filter(age__gt=22)


# # Age less than 22
# Student.objects.filter(age__lt=22)


# # Filter names using __in
# Student.objects.filter(
#     name__in=["Krishna", "hari", "gopal"]
# )


# # Another __in example
# Student.objects.filter(
#     name__in=["Sita", "hari", "gopal"]
# )


# # ==========================================
# # COURSE QUERIES
# # ==========================================

# # Create Django course
# Course.objects.create(name="Django")


# # Create Python course
# Course.objects.create(name="Python")


# # Create Java course
# Course.objects.create(name="Java")


# # Create Javascript course
# Course.objects.create(name="Javascript")


# # Create English course
# Course.objects.create(name="English")


# # Get all courses
# Course.objects.all()


# # Get all courses as dictionaries
# Course.objects.all().values()


# # Get Django course
# Django = Course.objects.get(id=1)


# Get course by name
# Dj = Course.objects.get(name="Django")


# ==========================================
# ASSIGN COURSE TO STUDENT
# ==========================================

# Get Django course
# Django = Course.objects.get(id=1)


# Get Ram
# Ram = Student.objects.get(id=2)


# Assign Django course to Ram
# Ram.course = Django


# Save Ram
# Ram.save()


# Print Ram's course
# print(Ram.course)


# Get Abhi
# Abhi = Student.objects.get(id=1)


# Assign Django course to Abhi
# Abhi.course = Django


# Save Abhi
# Abhi.save()


# Print Abhi's course
# print(Abhi.course)


# ==========================================
# UPDATE MULTIPLE STUDENTS
# ==========================================

# Assign Django to students with ID less than 5
# Student.objects.filter(id__lt=5).update(course=Django)


# Get Python course
# Python = Course.objects.get(id=2)


# Assign Python to students with ID greater than 1
# Student.objects.filter(id__gt=1).update(course=Python)


# ==========================================
# COURSE RELATIONSHIP QUERIES
# ==========================================

# Get students whose course is Python
# Student.objects.filter(course__name="Python")


# Get students whose course is Django
# Student.objects.filter(course__name="Django")


# Get all students enrolled in Python
# Course.objects.get(name="Python").students.all()


# Get courses having students older than 20
# Course.objects.filter(students__age__gt=20)


# ==========================================
# STUDENT PROFILE
# ==========================================

# Get Ram
# Ram = Student.objects.get(id=2)


# Create profile for Ram
# StudentProfile.objects.create(
#     student=Ram,
#     phone="984289875",
#     university="TU"
# )


# Get all student profiles
# StudentProfile.objects.all()


# Get all profiles as dictionaries
# StudentProfile.objects.all().values()


# Get Ram's profile
# Ram_profile = StudentProfile.objects.get(id=1)


# Get student from profile
# Ram_profile.student


# Get phone number
# Ram_profile.phone


# Get university
# Ram_profile.university


# ==========================================
# EXIT DJANGO SHELL
# ==========================================

#exit()


