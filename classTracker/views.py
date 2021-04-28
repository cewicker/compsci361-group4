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
        course.course_name = request.POST.get('course_name')
        course.course_no = request.POST.get('course_no')
        course.section_no = request.POST.get('section_no')
        course.is_lab = request.POST.get('is_lab') == "on"
        print(course.course_no)
        print(course.section_no)
        print(course.course_name)
        if course.course_no == "" or course.course_name == "" or course.section_no == "":
            return render(request, "create_course.html", {"message": "ERROR: all fields must be filled out"})
        else:
            course.save()
            return redirect("/courses")

class create_User(View):
    def get(self, request):
        return render(request, "create_user.html", {})

    def post(self, request):
        first_name = request.POST.get['name']
        last_name = request.POST.get['last_name']
        user_id = request.POST.get['user_id']
        number = request.POST.get['phone_number']
        role = request.POST.get['role']
        assignment_id = request.POST.get['assignment_ID']
        email = request.POST.get['email']

        user = User(first_name=first_name, last_name=last_name, id=user_id, number=number, role=role,
                    assignment_ID=assignment_id, email=email)
        error_dict = []
        error_dict = validate_user(user)

        if not error_dict:
            user.save()
            return render(request, "create_user.html", {})
        else:
            return render(request, "create_user.html", {"errors": error_dict})