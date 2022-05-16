from dataclasses import fields

from accounts.models import TeacherPorfile
from accounts.serializer import (StudentProfileSerialzer,
                                 TeacherProfileSerialzer)
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from .models import (Classes, CourseContent, CourseContentFile,
                     CourseContentVideo, Courses, HomeWork, HomeWorkSubmission,
                     JoinClasses)


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
class JoinClassesClassSerialzer(ModelSerializer):
    # students=StudentProfileSerialzer(many=True, read_only=True)
    class_sec=ClassesSerialzer(read_only=True)
    class Meta:
        model = JoinClasses
        fields = ['class_sec']

class CourseSerialzer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        depth=3


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

class CourseContentVideoSerializer(ModelSerializer):
    class Meta:
        model=CourseContentVideo
        fields='__all__'

class HomeworkSerializer(ModelSerializer):
    class Meta:
        model = HomeWork
        fields = '__all__'
        extra_kwargs = {'file': {'required': False}}


class HomeworkSubmissionSerializer(ModelSerializer):
    class Meta:
        model = HomeWorkSubmission
        fields = '__all__'
        depth=2
        extra_kwargs = {'file': {'required': False},'answer': {'required': False},'student': {'required': False},'homework_no': {'required': False}}



class HomeworkResultSerializer(ModelSerializer):
    class Meta:
        model = HomeWorkSubmission
        fields = ["student", "marks","homework_no"]
        depth=3
        # extra_kwargs = {'file': {'required': False},'answer': {'required': False},'student': {'required': False},'homework_no': {'required': False}}


