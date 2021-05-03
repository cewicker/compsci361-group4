from django.db import models


# Create your models here.
class Course(models.Model):
    course_no = models.CharField(max_length=200, default="")
    section_no = models.CharField(max_length=200, default="")
    course_name = models.CharField(max_length=200, default="")
    meeting_times = models.CharField(max_length=200, default="")
    is_lab = models.BooleanField(default=False)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default="")
    user_name = models.CharField(max_length=50, default="", unique=True)
    user_id = models.CharField(max_length=50,unique=True)
    number = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    assignment_ID = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50,unique=True)
