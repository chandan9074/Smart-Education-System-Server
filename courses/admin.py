from django.contrib import admin
from courses.models import Classes, Courses, JoinClasses
# Register your models here.

admin.site.register(Classes)
admin.site.register(JoinClasses)
admin.site.register(Courses)