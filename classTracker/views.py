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