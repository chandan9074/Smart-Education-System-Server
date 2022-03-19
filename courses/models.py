from pyexpat import model
from django.db import models

from accounts.models import StudentPorfile, TeacherPorfile
# Create your models here.

class Classes(models.Model):
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=20)

    def __str__(self):
        return (self.class_name)+(self.section)


class JoinClasses(models.Model):
    class_sec=models.ForeignKey(Classes, on_delete=models.CASCADE)
    students = models.ManyToManyField(StudentPorfile)

    def __str__(self):
        return (self.class_sec.class_name)+(self.class_sec.section)


class Courses(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    course_code = models.CharField(max_length=100)
    classes = models.ManyToManyField(JoinClasses)
    instructor = models.ForeignKey(TeacherPorfile, on_delete=models.CASCADE, null=True)

class CourseContent(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    links = models.TextField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

class CourseContentFile(models.Model):
    file = models.FileField()
    course_content = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    

