from django.contrib import admin
from courses.models import Classes, Courses, HomeWork, HomeWorkSubmission, JoinClasses, CourseContent, CourseContentFile, CourseContentVideo


admin.site.register(Classes)
admin.site.register(JoinClasses)
admin.site.register(Courses)
admin.site.register(CourseContent)
admin.site.register(CourseContentFile)
admin.site.register(HomeWork)
admin.site.register(HomeWorkSubmission)
admin.site.register(CourseContentVideo)
