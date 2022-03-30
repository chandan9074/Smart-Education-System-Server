from django.urls import path

from .views import *

urlpatterns = [
    path('course-view/', CourseAPIView.as_view(), name="course-view"),
    path('student-courses/<str:username>', StudentsCourseView.as_view(), name="student-courses"),
    path('course-details/<int:pk>', CourseDetailsAPIView.as_view(), name="course-details"),
    path('classes-view/', ClassesAPIView.as_view(), name="course-view"),
    path('classes-details/<int:pk>', ClassesDetailsAPIView.as_view(), name="course-details"),
    path('course-content-view/', CourseContentAPIView.as_view(), name="course-content-view"),
    path('course-content-details/<int:pk>', CourseContentDetailsAPIView.as_view(), name="course-content-details"),
    path('course-content-file-view/', CourseContentFileAPIView.as_view(), name="course-content-file-view"),
    path('course-content-file-details/<int:pk>', CourseContentFileDetailsAPIView.as_view(), name="course-content-file-details"),
    path('homework-details/<int:pk>', HomeWorkDetailsAPIView.as_view(), name="homework-details"),
    path('homework/', HomeWorkAPIView.as_view(), name="homework-details-details"),
    path('homework-submission/<int:pk>', HomeWorkSubmissionAPIView.as_view(), name="homework-submission"),
    path('student-submission/<int:pk>', StudentsSubmissionAPIView.as_view(), name="stdent-submission"),
    path('update-marks/<int:pk>', UpdateHomeworkMarksAPIView.as_view(), name="update-marks"),
]
