from django.urls import path

from .views import *

urlpatterns = [
    path('yearly-result/', YearlyResultAPIView.as_view(), name="yearly-result-view"),
    path('students-yearly-result/<str:username>', StudentsYearlyResultAPIView.as_view(), name="yearly-result-view"),
    path('yearly-result-details/<int:pk>', YearlyResultDetailsAPIView.as_view(), name="yearly-result-details-view"),
]
