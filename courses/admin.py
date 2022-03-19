from django.contrib import admin
from courses.models import Classes, Courses, CourseContent, CourseContentFile
# Register your models here.

admin.site.register(Classes)
admin.site.register(Courses)
admin.site.register(CourseContent)
admin.site.register(CourseContentFile)