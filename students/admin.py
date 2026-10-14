from django.contrib import admin
from .models import Course, Student, StudentProfile, Subject

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Course)
admin.site.register(Subject)
