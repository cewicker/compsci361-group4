"""classTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from classTracker.views import Home, Courses, CreateCourse, CreateUser, LoginView, courseAssignment, EditCourse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home.as_view()),
    path('courses/', Courses.as_view()),
    path('courses/create_course', CreateCourse.as_view(), name="createCourse"),
    path('courses/create_course<int:courseId>', EditCourse.as_view(), name="createCourse"),
    path('create_user/', CreateUser.as_view()),
    path('', LoginView.as_view()),
    path('assign_to_course/', courseAssignment.as_view()),
]
