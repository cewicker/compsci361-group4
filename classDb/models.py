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