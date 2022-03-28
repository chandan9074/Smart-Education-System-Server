from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type = {
        ("student", "Student"),
        ("teacher", "Teacher")
    }
    type = models.CharField(max_length=100, choices=user_type)


class StudentPorfile(models.Model):
    guardian = models.CharField(max_length=200, blank=True)
    guardian_phone_no = models.CharField(max_length=20, blank=True)
    relation = models.CharField(max_length=100, blank=True)
    blood_group = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=300, blank=True)
    dob = models.CharField(max_length=50, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class TeacherPorfile(models.Model):
    phone_no = models.CharField(max_length=20, blank=True)
    blood_group = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=300, blank=True)
    dob = models.CharField(max_length=50, blank=True)


    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username