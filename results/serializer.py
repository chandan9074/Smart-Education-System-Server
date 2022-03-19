from rest_framework.serializers import ModelSerializer
from .models import *
from courses.serializer import ClassesSerialzer
from accounts.serializer import StudentProfileSerialzer

class YearlyResultSerializer(ModelSerializer):
    class_name=ClassesSerialzer(read_only=True)
    students=StudentProfileSerialzer(read_only=True)

    class Meta:
        model = YearlyResult
        fields = '__all__'