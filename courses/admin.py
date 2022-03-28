from django.contrib import admin
from courses.models import Classes, Courses, JoinClasses, CourseContent, CourseContentFile


admin.site.register(Classes)
admin.site.register(JoinClasses)
admin.site.register(Courses)
admin.site.register(CourseContent)
admin.site.register(CourseContentFile)
