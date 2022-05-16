from asyncio.windows_events import NULL
from functools import partial

from accounts.models import StudentPorfile, TeacherPorfile, User
from accounts.serializer import StudentProfileSerialzer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Classes, CourseContent, CourseContentFile,
                     CourseContentVideo, Courses, HomeWork, HomeWorkSubmission,
                     JoinClasses)
from .serializer import (ClassesSerializer, CourseContentFileSerializer,
                         CourseContentSerializer, CourseContentVideoSerializer,
                         CourseSerialzer, HomeworkSerializer,
                         HomeworkSubmissionSerializer,
                         JoinClassesClassSerialzer, JoinClassesSerialzer)


class CourseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = User.objects.get(username=request.user)
            
            if user.type=="student":
                coursess=[]
                userprofile=StudentPorfile.objects.get(user=user)
                for cls in JoinClasses.objects.all():
                    if cls.students.filter(id=userprofile.id):
                        for course in Courses.objects.all():
                            clasName = course.classes.filter(id=cls.id)
                            if clasName:
                                coursess.append(Courses.objects.get(id=course.id))

                course_serializer = CourseSerialzer(coursess, many=True)

                return Response(course_serializer.data, status=status.HTTP_200_OK)

            elif user.type=="teacher":
                userprofile=TeacherPorfile.objects.get(user=user)
                courses = Courses.objects.filter(instructor=userprofile.id)
                course_serializer = CourseSerialzer(courses, many=True)
                return Response(course_serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CourseSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentsCourseView(APIView):

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

    def get(self, request, pk):
        if(CourseContent.objects.filter(courses=pk)).exists():
            course_content = CourseContent.objects.filter(courses=pk)
            course_content_serializer = CourseContentSerializer(course_content, many=True)
            return Response(course_content_serializer.data, status=status.HTTP_200_OK)


class CourseContentPostAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
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


class CourseContentFileByContentAPiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if(CourseContentFile.objects.filter(course_content=pk)).exists():
            course_content = CourseContentFile.objects.filter(course_content=pk)
            course_content_serializer = CourseContentFileSerializer(course_content, many=True)
            return Response(course_content_serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CourseContentVideoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CourseContentVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
class HomeWorkAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        homework = HomeWork.objects.all()
        homework_serializer = HomeworkSerializer(homework, many=True)

        return Response(homework_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.course_content=(CourseContent.objects.get(id=request.data["course_content"]))
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseContentVideoDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        if(CourseContentVideo.objects.filter(id=pk)).exists():
            serializer_del = CourseContentVideo.objects.get(id=pk)
            serializer_del.delete()
            return Response({"msg": "delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CourseContentGetVideoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if(CourseContentVideo.objects.filter(course_content=pk)).exists():
            course_content = CourseContentVideo.objects.filter(course_content=pk)
            course_content_serializer = CourseContentVideoSerializer(course_content, many=True)
            return Response(course_content_serializer.data, status=status.HTTP_200_OK)

class HomeWorkDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        homework = HomeWork.objects.get(id=pk)
        homework_serializer = HomeworkSerializer(homework)

        return Response(homework_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        homework_obj = HomeWork.objects.get(id=pk)
        serializer = HomeworkSerializer(homework_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if(HomeWork.objects.filter(id=pk)).exists():
            obj_del = HomeWork.objects.get(id=pk)
            obj_del.delete()
            return Response({"msg": "delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class HomeWorkSubmissionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        homeworks = HomeWorkSubmission.objects.filter(homework_no=pk)
        homework_serializer = HomeworkSubmissionSerializer(homeworks, many=True)

        return Response(homework_serializer.data, status=status.HTTP_200_OK)

    def post(self, request,pk):
        home_work=HomeWorkSubmission.objects.create(submission_time=request.data["submission_time"],submitted_file=request.data["submitted_file"],answer=request.data["answer"],marks=request.data["marks"],homework_no=(HomeWork.objects.get(id=pk)),student=(StudentPorfile.objects.get(user=(User.objects.get(username=request.user).id))))

        home_work.save()
        homework_serializer=HomeworkSubmissionSerializer(home_work)
        return Response(homework_serializer.data, status=status.HTTP_200_OK)
        # return Response(homework_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateHomeworkMarksAPIView(APIView):

    def put(self, request, pk):
        homework_obj = HomeWorkSubmission.objects.get(id=pk)
        serializer = HomeworkSubmissionSerializer(homework_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsSubmissionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        user_profile=StudentPorfile.objects.get(user=(User.objects.get(username=request.user).id)).id
        homeworks = HomeWorkSubmission.objects.get(homework_no=pk, student=user_profile)
        homework_serializer = HomeworkSubmissionSerializer(homeworks)

        return Response(homework_serializer.data, status=status.HTTP_200_OK)
        
class HomeworkDetailsByContentsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = HomeWork.objects.filter(course_content=pk)
            course_content = HomeWork.objects.filter(course_content=pk)
            content_homework_serializer = HomeworkSerializer(course_content, many=True)
            return Response(content_homework_serializer.data, status=status.HTTP_200_OK)

        except HomeWork.DoesNotExist:
            return Response({"msg":"No Homeworks"}, status=status.HTTP_404_NOT_FOUND)
        
class ClassDetailsByStudentView(APIView):

    def get(self, request, username):
        if(JoinClasses.objects.filter(students__user__username=username)).exists():
            user = JoinClasses.objects.filter(students__user__username=username)
            class_serializer = JoinClassesClassSerialzer(user, many=True)

            return Response(class_serializer.data, status=status.HTTP_200_OK)
        return Response({"msg":"No user"}, status=status.HTTP_404_NOT_FOUND)

# class StudentView(APIView):
#     def get(self, request, pk):
#         if(JoinClasses.objects.filter(students__id=pk)).exists():
#             user = JoinClasses.objects.filter(students__id=pk)
#             class_serializer = JoinClassesSerialzer(user, many=True)

#             return Response(class_serializer.data, status=status.HTTP_200_OK)
