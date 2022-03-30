from django.urls import path

from .views import *

urlpatterns = [
    path('course-view/', CourseAPIView.as_view(), name="course-view"),
    path('student-courses/<str:username>', StudentsCourseView.as_view(), name="student-courses"),
    path('course-details/<int:pk>', CourseDetailsAPIView.as_view(), name="course-details"),
    path('classes-view/', ClassesAPIView.as_view(), name="course-view"),
    path('classes-details/<int:pk>', ClassesDetailsAPIView.as_view(), name="course-details"),
    path('course-content-view/<int:pk>', CourseContentAPIView.as_view(), name="course-content-view"),
    path('course-content-post/', CourseContentPostAPIView.as_view(), name="course-content-post"),
   
    path('course-content-details/<int:pk>', CourseContentDetailsAPIView.as_view(), name="course-content-details"),
    path('course-content-file-view/', CourseContentFileAPIView.as_view(), name="course-content-file-view"),
    
    path('course-content-video-view/', CourseContentVideoAPIView.as_view(), name="course-content-video-view"),
    path('course-content-video-details/<int:pk>', CourseContentVideoDetailsAPIView.as_view(), name="course-content-video-details"),
    path('course-content-video-get/<int:pk>', CourseContentGetVideoAPIView.as_view(), name="course-content-video-get"),

    path('course-content-file-details/<int:pk>', CourseContentFileDetailsAPIView.as_view(), name="course-content-file-details"),
    path('course-content-file-details-by-content/<int:pk>', CourseContentFileByContentAPiView.as_view(), name="course-content-file-details-by-content"),
    
    path('homework-details/<int:pk>', HomeWorkDetailsAPIView.as_view(), name="homework-details-details"),
]
