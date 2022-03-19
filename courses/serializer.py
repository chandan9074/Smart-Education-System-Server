from ast import Mod
from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from accounts.serializer import StudentProfileSerialzer
from .models import Classes, Courses, JoinClasses

class ClassesSerialzer(ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class JoinClassesSerialzer(ModelSerializer):
    students=StudentProfileSerialzer(many=True, read_only=True)
    class_sec=ClassesSerialzer(read_only=True)
    class Meta:
        model = JoinClasses
        fields = '__all__'

class CourseSerialzer(ModelSerializer):
    classes=JoinClassesSerialzer(many=True,read_only=True)
    class Meta:
        model = Courses
        fields = '__all__'