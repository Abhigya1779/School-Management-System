import json
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import AIConversation,Student,Course, Subject
from students.forms import StudentForm
from django.http import JsonResponse
from django.http import JsonResponse

# from django.http import HttpResponse
def course_data(request, student_id):
    course = Course.objects.get(id=student_id)
    data = {
        "id": course.id,
        "name": course.name,
    }
    return JsonResponse(data)


def course_data_create(request):

    if request.method == "POST":

        data = json.loads(request.body)

        course = Course.objects.create(
            name=data["name"],
        )

        return JsonResponse({
            "message": "Course created",
            "id": course.id
        })
 

# Create your views here.
def home(request):
   #return HttpResponse("Hello Django!")
   return render(request, 'students/home.html')

def about(request):
    return render(request, 'students/about.html')

def profile(request):
    return render(request, 'students/profile.html')

def student_list(request):
    students = Student.objects.all()
    return render(
        request,
          'students/list_student.html',
           {'students': students
           })

def courses(request):
    courses = Course.objects.all()
    return render(
        request,
          'students/list_course.html',
           {'courses': courses
           })

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(
        request,
          'students/student_detail.html',
           {'student': student
           })

def student_data(request, student_id):
    student = Student.objects.get(id=student_id)
    data = {
        "id":student.id,
        "name":student.name,
        "age":student.age,
        "address":student.address
    }
    return JsonResponse(data)

def subject_list(request):
    subjects = Subject.objects.all()
    return render(
        request,
          'students/subject_list.html',
           {'subjects': subjects
           })

# v1
# def student_create(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         age = request.POST.get("age")
#         address = request.POST.get("address")
#         course_id = request.POST.get("course_id")
 
#         Student.objects.create(
#             name=name,
#             email=email,
#             age=age,
#             address=address,
#             course_id=course_id
#         )
 
#         return redirect("student_list")
    
#     courses = Course.objects.all()
 
#     return render(
#         request,
#         "students/student_create.html",
#         {"courses": courses}
#     )
# @Permission_required("students.add_students")
def students_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        #     name = form.cleaned_data['name']
        #     email = form.cleaned_data['email']
        #     age = form.cleaned_data['age']
        #     address = form.cleaned_data['address']

        # Student.objects.create(
        #     name=name, 
        #     email=email, 
        #     age=age, 
        #     address=address,
        #     )
        
            return redirect('student_list')
    else:
        form = StudentForm()

    # courses = Course.objects.all() 

    return render(request, 'students/student_create.html', 
                  {"form": form})


def course_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        Course.objects.create(
            name=name,  
            )
        
        return redirect('courses')

    return render(request, 'students/course_create.html')

from .ai_service import ask_ai

def ai_chat(request):
    answer = ""
    question = ""
    error = ""

    if request.method == "POST":
        question = request.POST.get("question", "").strip()

        if question:
            try:
                answer = ask_ai(question)

                AIConversation.objects.create(
                    question=question,
                    answer=answer,
                )
            except Exception as e:
                error = f"Sorry, the AI service is unavailable. {e}"

    conversations = AIConversation.objects.order_by("-created_at")

    return render(
        request,
        "students/ai_chat.html",
        {
            "question": question,
            "answer": answer,
            "error": error,
            "conversations": conversations,
        },
    )
 
