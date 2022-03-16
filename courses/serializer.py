from ast import Mod
from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Courses

class CourseSerialzer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'