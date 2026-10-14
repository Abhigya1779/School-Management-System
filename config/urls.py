"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from students.views import about, ai_chat, course_create, course_data, course_data_create, home, profile, student_detail, student_list, courses, students_create, subject_list, student_data
from accounts.views import register,profile
from django.contrib.auth import views as auth_views
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list, name='home'),
    path("about/", about, name='about'),
    path("profile/", profile, name='profile'),
    path("students/", student_list, name='student_list'),
    path("students/create/", students_create, name='student_create'),
    path("courses/create/", course_create, name='course_create'),
    path("courses/", courses, name='course_list'),
    path("student/<int:student_id>/", student_detail, name='student_detail'),
    path("subjects/", subject_list, name='subject_list'),
    path("register/", register, name='register'),
    path("profile/", profile, name="profile"),
    path("student_data/<int:student_id>/", student_data, name="student_data"),
    path("course-data/<int:student_id>/", course_data, name="course_data"),
    path("course-data/create/", course_data_create, name="course_create"),
    path("ai-chat/", ai_chat, name="ai_chat"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            next_page="student_list"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

path("api/", include("students.urls_api")),
path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
