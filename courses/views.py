from rest_framework.response import Response
from django.shortcuts import render
from .serializer import CourseSerialzer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Courses
# Create your views here.


class CourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        course = Courses.objects.all()
        course_serializer = CourseSerialzer(course, many=True)

        return Response(course_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        course = self.get_object(pk)
        course_serializer = CourseSerialzer(course)
        return Response(course_serializer.data)

    def put(self, request, pk):
        course_obj = Courses.objects.get(id=pk)
        serializer = CourseSerialzer(course_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if(Courses.objects.filter(id=pk)).exists():
            serializer_del = Courses.objects.get(id=pk)
            serializer_del.delete()
            return Response({"msg": "delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


