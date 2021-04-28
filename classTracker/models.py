from django.db import models

#Create your models here.
class Course(models.Model):
    course_no = models.CharField(max_length=200)
    section_no = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    meeting_times = models.CharField(max_length=200)
    is_lab = models.BooleanField()

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    assignment_ID = models.CharField(max_length=50)
    email = models.CharField(max_length=50)