from django.shortcuts import render, redirect
from django.views import View
from classTracker.models import User
from .validateFunction import validate_user


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})


class Courses(View):
    def get(self, request):
        return render(request, "courses.html", {})


class CreateCourse(View):
    def get(self, request):
        return render(request, "create_course.html", {})


class CreateUser(View):
    def get(self, request):
        return render(request, "create_user.html", {})

    def post(self, request):
        first_name = request.POST['name']
        last_name = request.POST['lastName']
        user_id = request.POST['user_ID']
        number = request.POST['phone_number']
        role = request.POST['role']
        assignment_id = request.POST['assignment_ID']
        email = request.POST['email']

        user = User(first_name=first_name, last_name=last_name, id=user_id, number=number, role=role,
                    assignment_ID=assignment_id, email=email)
        error_dict = []
        error_dict = validate_user(user)

        if not error_dict:
            user.save()
            return render(request, "create_user.html", {})
        else:
            return render(request, "create_user.html", {"errors": error_dict})
