from ast import Mod
from dataclasses import field, fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Courses, Classes

class CourseSerialzer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class ClassesSerializer(ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'