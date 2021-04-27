from django.shortcuts import render, redirect
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, "home.html", {})

class Courses(View):
    def get(self, request):
        return render(request, "courses.html", {})

class CreateCourse(View):
    def get(self, request):
        return render(request, "create_course.html", {})
