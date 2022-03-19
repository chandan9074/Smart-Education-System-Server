from django.urls import path

from .views import *

urlpatterns = [
    path('course-view/', CourseAPIView.as_view(), name="course-view"),
    path('student-courses/<str:username>', StudentsCourse.as_view(), name="student-courses"),
    path('course-details/<int:pk>', CourseDetailsAPIView.as_view(), name="course-details"),
]
