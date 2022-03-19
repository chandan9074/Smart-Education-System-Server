from rest_framework.serializers import ModelSerializer
from .models import Courses, Classes, CourseContent, CourseContentFile

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