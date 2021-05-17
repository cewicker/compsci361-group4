from django.shortcuts import render, redirect
from django.views import View
from classTracker.models import User, Course
from .validateFunction import validate_user
from django.db import IntegrityError


class Home(View):
    def get(self, request):
        user_name = request.session['user_name']
        user = User.objects.get(user_name = request.session['user_name'])
        course_list = list(Course.objects.filter(instructor = user))

        return render(request, "home.html", {'course_list': course_list})


class Courses(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "courses.html", {'courses': courses})

    def post(self, request):
        return redirect("/courses/create_course", {'course_id': request.POST.get})


class EditCourse(View):
    def get(self, request, courseId):
        course = Course.objects.get(id=courseId)
        return render(request, "create_course.html",
                      {'course_name_in': course.course_name, 'course_no_in': course.course_no,
                       'meeting_times_in': course.meeting_times, 'section_no_in': course.section_no,
                       'is_lab_in': course.is_lab, 'course_id_in': courseId, 'edit_mode': True})

    def post(self, request, courseId):
        course = Course.objects.get(id=courseId)
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
            return redirect("/courses", {'course_name': course.course_name})


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

        user = User(first_name=first_name, user_name=user_name, last_name=last_name, password=password, user_id=user_id,
                    number=number, role=role,
                    assignment_ID=assignment_id, email=email)
        error_dict = []
        error_dict = validate_user(user)
        valid = ["User successfully created"]

        if not error_dict:
            try:
                user.save()
            except IntegrityError:
                error_dict.append("user_name / user_id already exists")
                return render(request, "create_user.html", {"errors": error_dict})
            else:
                return render(request, "create_user.html", {"errors": valid})
        else:
            return render(request, "create_user.html", {"errors": error_dict})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        error = "Incorrect password/username try again"
        log_dict = []
        noSuchUser = False
        badPassword = False
        if request.POST['user_name'] == "admin":
            return redirect('/home')
        try:

            m = User.objects.get(user_name=request.POST['user_name'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:

            log_dict.append(error)
            log_dict.append("noSuchUser")
            return render(request, "login.html", {"login_errors": log_dict})
        elif badPassword:
            log_dict.append(error)
            return render(request, "login.html", {"login_errors": log_dict})
        else:
            request.session['user'] = m.user_name
            request.session.modified = True
            return redirect("/home")



class EditUser(View):
    def get(self, request, userId):
        user = User.objects.get(id=userId)
        return render(request, "create_user.html", {'first_name_in': user.first_name, 'last_name_in': user.last_name, 'password_in': user.password, 'user_name_in': user.user_name, 'user_id_in': user.user_id, 'number_in': user.number, 'role_in': user.role, 'assignment_ID_in': user.assignment_ID, 'email_in': user.email, 'edit_mode': True})

    def post(self, request, userId):
        user = User.objects.get(id=userId)
        first_name = request.POST['name']
        last_name = request.POST['lastName']
        user_name = request.POST['user_name']
        user_id = request.POST['user_id']
        number = request.POST['phone_number']
        role = request.POST['role']
        assignment_id = request.POST['assignment_id']
        email = request.POST['email']
        password = request.POST['password']

        user = User(first_name=first_name, user_name=user_name, last_name=last_name, password=password, user_id=user_id,
                    number=number, role=role,
                    assignment_ID=assignment_id, email=email)

        error_dict = []
        error_dict = validate_user(user)
        valid = ["User successfully edited"]

        if not error_dict:
            try:
                user.save()
            except IntegrityError:
                error_dict.append("user_name / user_id already exists")
                return render(request, "create_user.html", {"errors": error_dict})
            else:
                return render(request, "create_user.html", {"errors": valid})
        else:
            return render(request, "create_user.html", {"errors": error_dict})
class courseAssignment(View):
    def get(self, request):
        course_list = list(Course.objects.all())
        instructor_list = list(User.objects.all())
        return render(request, "assign_to_course.html", {"course_list": course_list, "user_list": instructor_list})

    def post(self, request):
        course_list = list(Course.objects.all())
        instructor_list = list(User.objects.all())

        instructor_1 = request.POST['instructor']
        instructor_array = instructor_1.split()

        instructor_obj = User.objects.get(first_name=instructor_array[0], last_name=instructor_array[1])

        courseName2 = request.POST['course_name']

        courseObject = Course.objects.get(course_name=courseName2)
        courseObject.instructor=instructor_obj
        courseObject.save()

        return render(request, "assign_to_course.html",
                      {"course_list": course_list, "user_list": instructor_list})
