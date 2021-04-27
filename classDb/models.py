from django.db import models


# Create your models here.

class Course(models.Model):
    course_id = models.IntegerField
    section_no = models.IntegerField
    course_name = models.CharField
    is_lab = models.BooleanField


class CourseAssignment(models.Model):
    course_id = models.ForeignKey
    user_id = models.ForeignKey


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    assignment_ID = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
