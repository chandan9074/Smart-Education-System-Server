from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type = {
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("guardian", "Guardian")
    }
    type = models.CharField(max_length=100, choices=user_type)