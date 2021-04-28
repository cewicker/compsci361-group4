from django.shortcuts import render, redirect
from django.views import View
from .models import Course

class Home(View):
    def get(self, request):
        return render(request, "home.html", {})

class Courses(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "courses.html", {'courses': courses})

class CreateCourse(View):
    def get(self, request):
        return render(request, "create_course.html", {})
    def post(self, request):
        course = Course()
        course.course_name=request.POST.get('course_name')
        course.course_no = request.POST.get('course_no')
        course.section_no=request.POST.get('section_no')
        course.is_lab = request.POST.get('is_lab') == "on"
        print(course.course_no)
        print(course.section_no)
        print(course.course_name)
        print(course.is_lab)
        course.save()
        return redirect("/courses")
