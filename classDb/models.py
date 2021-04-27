from django.db import models


#Create your models here.
class Course(models.Model):
    course_no = models.IntegerField
    section_no = models.IntegerField
    course_name = models.CharField
    is_lab = models.BooleanField
    app_label = 'coursemodel'
