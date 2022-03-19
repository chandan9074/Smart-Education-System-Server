from ast import Mod
from dataclasses import field, fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Courses, Classes, CourseContent, CourseContentFile

class CourseSerialzer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class ClassesSerializer(ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class CourseContentSerializer(ModelSerializer):
    class Meta:
        model = CourseContent
        fields = '__all__'

class CourseContentFileSerializer(ModelSerializer):
    class Meta:
        model = CourseContentFile
        fields = '__all__'