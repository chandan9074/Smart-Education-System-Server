from django.db import models

# Create your models here.

class Courses(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    course_code = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20)
    
