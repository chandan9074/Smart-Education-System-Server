from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.SignUpView.as_view()),
    path('verification/', views.verification, name='activate'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('authenticate-student/', views.AuthenticateStudent.as_view(), name="authenticate_student"),
    path('logout/', views.LogoutView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('user/<str:username>/', views.UserView.as_view()),
]