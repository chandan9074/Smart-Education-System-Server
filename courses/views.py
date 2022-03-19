from rest_framework.response import Response
from accounts.models import StudentPorfile, User
from .serializer import CourseSerialzer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Classes, Courses, JoinClasses
# Create your views here.


class CourseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        coursess=[]
        userprofile=StudentPorfile.objects.get(user=User.objects.get(username=request.user))
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


