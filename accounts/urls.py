from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.SignUpView.as_view()),
    path('verification/', views.verification, name='activate'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view()),
]