from django.urls import path

from .views import *

urlpatterns = [
    path('course-view/', CourseAPIView.as_view(), name="course-view"),
    path('course-details/<int:pk>', CourseDetailsAPIView.as_view(), name="course-details"),
    path('classes-view/', ClassesAPIView.as_view(), name="course-view"),
    path('classes-details/<int:pk>', ClassesDetailsAPIView.as_view(), name="course-details"),
]
