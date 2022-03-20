from rest_framework.response import Response
from accounts.models import StudentPorfile, User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import CourseSerialzer, ClassesSerializer, CourseContentSerializer, CourseContentFileSerializer
from .models import Courses, Classes, CourseContent, CourseContentFile, JoinClasses


class CourseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        coursess=[]
        userprofile=StudentPorfile.objects.get(user=User.objects.get(username=request.user))
        for cls in JoinClasses.objects.all():
            if cls.students.filter(id=userprofile.id):
                for course in Courses.objects.all():
                    clasName = course.classes.filter(id=cls.id)
                    if clasName:
                        coursess.append(Courses.objects.get(id=course.id))

        course_serializer = CourseSerialzer(coursess, many=True)

        return Response(course_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentsCourse(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,username):
        coursess=[]
        userprofile=StudentPorfile.objects.get(user=User.objects.get(username=username))
        # print(userprofile.id)
        for cls in JoinClasses.objects.all():
            if cls.students.filter(id=userprofile.id):
                # print(cls.students.filter(user=userprofile.id))
                # if cls.classses.filter(id=Classes.objects.get(id=cls.id).id):
                for course in Courses.objects.all():
                    # clasName = course.classes.filter(id=Classes.objects.get(id=cls.id).id)
                    clasName = course.classes.filter(id=cls.id)

                    if clasName:
                        coursess.append(Courses.objects.get(id=course.id))
                    # print(Courses.objects.get(classes=clasName))

        # courses = Courses.objects.all()

        course_serializer = CourseSerialzer(coursess, many=True)

        return Response(course_serializer.data, status=status.HTTP_200_OK)


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


class ClassesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        classes = Classes.objects.all()
        classes_serializer = ClassesSerializer(classes, many=True)

        return Response(classes_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassesDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Classes.objects.get(pk=pk)
        except Classes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        classes = self.get_object(pk)
        classes_serializer = ClassesSerializer(classes)
        return Response(classes_serializer.data)

    def put(self, request, pk):
        classes_obj = Classes.objects.get(id=pk)
        serializer = ClassesSerializer(classes_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if(Classes.objects.filter(id=pk)).exists():
            serializer_del = Classes.objects.get(id=pk)
            serializer_del.delete()
            return Response({"msg": "delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CourseContentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        course_content = CourseContent.objects.all()
        course_content_serializer = CourseContentSerializer(course_content, many=True)

        return Response(course_content_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseContentDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CourseContent.objects.get(pk=pk)
        except CourseContent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        course_content = self.get_object(pk)
        course_content_serializer = CourseContentSerializer(course_content)
        return Response(course_content_serializer.data)

    def put(self, request, pk):
        course_content_obj = CourseContent.objects.get(id=pk)
        serializer = CourseContentSerializer(course_content_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if(CourseContent.objects.filter(id=pk)).exists():
            serializer_del = CourseContent.objects.get(id=pk)
            serializer_del.delete()
            return Response({"msg": "delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CourseContentFileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        course_content_file = CourseContentFile.objects.all()
        course_content_file_serializer = CourseContentFileSerializer(course_content_file, many=True)

        return Response(course_content_file_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseContentFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseContentFileDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CourseContentFile.objects.get(pk=pk)
        except CourseContentFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        course_content_file = self.get_object(pk)
        course_content_file_serializer = CourseContentFileSerializer(course_content_file)
        return Response(course_content_file_serializer.data)

    def put(self, request, pk):
        course_content_file_obj = CourseContentFile.objects.get(id=pk)
        serializer = CourseContentFileSerializer(course_content_file_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if(CourseContentFile.objects.filter(id=pk)).exists():
            serializer_del = CourseContentFile.objects.get(id=pk)
            serializer_del.delete()
            return Response({"msg": "delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)