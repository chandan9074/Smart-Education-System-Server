from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .utils import activation_token
from django.urls import reverse
from django.core.mail import send_mail
from django.urls import reverse
from decouple import config
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect

from .serializer import UserSerializer
from .models import User
# Create your views here.

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if(User.objects.filter(email=request.data["email"])):
            return Response({"msg": "Email Already Exist"}, status=status.HTTP_306_RESERVED)

        if(User.objects.filter(username=request.data["username"])):
            return Response({"msg": "Username Already Exist"}, status=status.HTTP_306_RESERVED)

        # profile_data = {
        #     "bio": "",
        #     "address": "",
        #     "website": "",
        #     'linkedin': "",
        #     'facebook': "",
        #     "github": "",
        #     "avatar": "",
        #     "email": "",
        #     "phone_no": ""
        # }

        if serializer.is_valid():
            # user_profile = Profile.objects.create(
            #     bio="", address="", website="", linkedin="", facebook="", github="", avatar="", email="", phone_no="")

            # user_profile.save()
            serializer.save()

            # user = (User.objects.get(username=serializer.data["username"]))
            # user.profile = Profile.objects.get(id=user_profile.id)
            # user.save()

            user = User.objects.get(email=serializer.data["email"])
            domain = get_current_site(request).domain
            uid = urlsafe_base64_encode(force_bytes(user.id))
            url = reverse('activate')
            token = uid + '.' + activation_token.make_token(user)
            activation_link = 'http://' + domain + url+'?token=' + token
            body = "Hi, " + user.first_name + " " + user.last_name + \
                "\nWelcome to Hackverse world.Click this link to varify your account.\n" + activation_link

            send_mail(
                'Account Varification',
                body,
                config('EMAIL_HOST_USER'),
                [user.email],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


def verification(request):
    received_token = request.GET['token']
    splited_token = received_token.split(".")
    uidb64 = splited_token[0]
    token = splited_token[1]
    account_activation_token = activation_token
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
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