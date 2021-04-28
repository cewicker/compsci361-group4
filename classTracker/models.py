from django.db import models


# Create your models here.

class Course(models.Model):
    course_no = models.CharField(max_length=200)
    section_no = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    is_lab = models.BooleanField()
