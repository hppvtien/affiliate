from allauth import socialaccount
from allauth.account.utils import user_field
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.utils.translation import gettext as _

from var_dump import var_dump
from django.core.files.storage import FileSystemStorage
from core import settings
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
import requests
import base64
import os, binascii
from user.models import share_link, share_link_page, create_share_link
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.


def dashboard(request):
    return render(request,"admin_user/dashboard.html")

def sign_up(request):
    return render(request,"admin_user/sign-up.html")
def sign_in(request):
    return render(request,"admin_user/sign-in.html")
def password_reset(request):
    return render(request,"admin_user/password-reset.html")
def new_password(request):
    return render(request,"admin_user/new-password.html")