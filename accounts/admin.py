from django.contrib import admin
from accounts.models import User, StudentPorfile, TeacherPorfile

# Register your models here.

admin.site.register(User)
admin.site.register(StudentPorfile)
admin.site.register(TeacherPorfile)