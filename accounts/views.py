from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str 
from rest_framework.authtoken.views import ObtainAuthToken
from .utils import activation_token
from decouple import config
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from .models import User, StudentPorfile, TeacherPorfile


class SignUpView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)

        if(User.objects.filter(email=request.data["email"])):
            return Response({"msg": "Email Already Exist"}, status=status.HTTP_306_RESERVED)

        if(User.objects.filter(username=request.data["username"])):
            return Response({"msg": "Username Already Exist"}, status=status.HTTP_306_RESERVED)

        if serializer.is_valid():
            serializer.save()
            user_type = request.data["type"]
            user_data = User.objects.get(username = request.data["username"])

            if(user_type == "student"):
                user_prof = StudentPorfile.objects.get(user = user_data.id)
                user_prof.dob=request.data["dob"]
                user_prof.save()
            elif(user_type == "teacher"):
                user_prof = TeacherPorfile.objects.get(user = user_data.id)
                user_prof.dob=request.data["dob"]
                user_prof.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


def verification(request):
    received_token = request.GET['token']
    splited_token = received_token.split(".")
    uidb64 = splited_token[0]
    token = splited_token[1]
    account_activation_token = activation_token
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user_token = (Token.objects.get(user_id=user.id)).key
        redirect_url = config('CLIENT_URL')+'success/?token=' + user_token

        return redirect(redirect_url)
    else:
        return redirect('/failed')


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'token': token.key
        })



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({"msg: Logged out"}, status=status.HTTP_200_OK)


class AuthenticateStudent(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.data["username"])
            if(StudentPorfile.objects.get(user=user.id).dob==request.data["dob"]):
                return Response({"username":user.username}, status=status.HTTP_200_OK)
            else:
                return Response({"msg":"DOB Doesn't Matched."}, status=status.HTTP_404_NOT_FOUND)

        except User.DoesNotExist:
            return Response({"msg":"User Doesn't Exist."}, status=status.HTTP_404_NOT_FOUND)