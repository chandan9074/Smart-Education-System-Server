from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.SignUpView.as_view()),
    path('verification/', views.verification, name='activate'),
]