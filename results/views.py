from functools import partial
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import StudentPorfile, User
from courses.models import Classes
from results.models import YearlyResult
from results.serializer import YearlyResultSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class YearlyResultAPIView(APIView):

    def get(self, request):
        results = YearlyResult.objects.all()
        result_serializer = YearlyResultSerializer(results, many=True)

        return Response(result_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        y_result=YearlyResult.objects.create(marks=request.data["marks"], total_marks=request.data["total_marks"], percentage=request.data["percentage"], comments=request.data["comments"], class_name=(Classes.objects.get(id=request.data["class_name"])), students=(StudentPorfile.objects.get(id=request.data["students"])))

        y_result.save()

        serializer = YearlyResultSerializer(y_result)
        return Response(serializer.data)

class YearlyResultDetailsAPIView(APIView):

    def get_object(self, pk):
        try:
            return YearlyResult.objects.get(pk=pk)
        except YearlyResult.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        result = self.get_object(pk)
        result_serializer = YearlyResultSerializer(result)
        return Response(result_serializer.data)

    def put(self, request, pk):
        result_obj = YearlyResult.objects.get(id=pk)
        result_obj.class_name=(Classes.objects.get(id=request.data["class_name"]))
        result_obj.students=(StudentPorfile.objects.get(id=request.data["students"]))

        serializer = YearlyResultSerializer(result_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if(YearlyResult.objects.filter(id=pk)).exists():
            serializer_del = YearlyResult.objects.get(id=pk)
            serializer_del.delete()
            return Response({"msg": "delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentsYearlyResultAPIView(APIView):

    def get(self, request, username):
        student=User.objects.get(username=username)
        student_profile=StudentPorfile.objects.get(user=student.id)
        results = YearlyResult.objects.filter(students=student_profile.id)
        result_serializer = YearlyResultSerializer(results, many=True)

        return Response(result_serializer.data, status=status.HTTP_200_OK)
        
