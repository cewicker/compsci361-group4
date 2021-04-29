from django.shortcuts import render, redirect
from django.views import View
from classTracker.models import User, Course
from .validateFunction import validate_user


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
        course.meeting_times = request.POST.get('meeting_times')
        course.section_no = request.POST.get('section_no')
        course.is_lab = request.POST.get('is_lab') == "on"
        if course.course_no == "" or course.course_name == "" or course.section_no == "" or course.meeting_times == "":
            return render(request, "create_course.html", {"message": "ERROR: all fields must be filled out"})
        else:
            course.save()
            return redirect("/courses")

class CreateUser(View):
    def get(self, request):
        return render(request, "create_user.html", {})

    def post(self, request):
        first_name = request.POST['name']
        last_name = request.POST['lastName']
        user_name = request.POST['user_name']
        user_id = request.POST['user_id']
        number = request.POST['phone_number']
        role = request.POST['role']
        assignment_id = request.POST['assignment_id']
        email = request.POST['email']
        password = request.POST['password']

        user = User(first_name=first_name, user_name=user_name, last_name=last_name, password=password, user_id=user_id, number=number, role=role,
                    assignment_ID=assignment_id, email=email)
        error_dict = []
        error_dict = validate_user(user)
        valid = ["User successfully created"]
        if not error_dict:
            user.save()
            return render(request, "create_user.html", {"errors": valid})
        else:
            return render(request, "create_user.html", {"errors": error_dict})

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        m = request.POST['user_name']
        error = "incorrect password/username"
        if m == "admin":
            return redirect('/home')
        else:
            return render(request, "login.html", {"login_errors": error})
