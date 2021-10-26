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
from SuperAdmin.models import super_admin
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


def user_admin(request):
    # super_admin_lish = super_admin.objects.filter(type=1)
    super_admin_lish = super_admin.objects.all()
    return render(request, "admin_user/page/useradmin/index.html", {"super_admin_lish": super_admin_lish})

def user_admin_create(request):
    return render(request,"admin_user/page/useradmin/create.html")

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'main/upload.html', {'file_url': file_url})
    
    
def user_admin_store(request):
   
    if request.method == "POST":
        store = super_admin()
        store.name = request.POST["name"]
        store.email = request.POST["email"]
        store.password = base64.b64encode(bytes(request.POST["password"], "utf-8")).decode()
        store.company = request.POST["company"]
        store.address = request.POST["address"]
        store.phone = request.POST["phone"]
        store.website = request.POST["website"]
        store.type = request.POST["type"]
        if len(request.FILES) != 0:
            store.avatar = request.FILES['avatar']
        store.save()
        # messages.success(request, "Product Added Successfully")
        return redirect('user-admin')
    return render(request, 'admin_user/page/useradmin/create.html')
        # avatar = request.FILES['avatar']
        # fss = FileSystemStorage()
        # file = fss.save(avatar.name, avatar)
        # file_url = fss.url(file)
            
        # try:
        #     obj = super_admin.objects.get(store.email=email)
        #     err_share_user_id = _("Code đã tồn tại")
        #     return render(request, "admin_user/page/useradmin/create.html", {"err_share_user_id": err_share_user_id})
           
        # except super_admin.DoesNotExist:
        #     obj = super_admin.objects.create(name=name, email=email, password=password, company=company, address=address, phone=phone, website=website, type=type, avatar=file_url)
        #     obj.save()
        #     return redirect("user-admin")
    # else:
    #     return render(request, "admin_user/page/useradmin/create.html")
    
def user_admin_edit(request, id):
    data_super_admin = super_admin.objects.get(id=id)
    return render(request, "admin_user/page/useradmin/edit.html", {"data_super_admin": data_super_admin})

def user_admin_update(request, id):
    # return HttpResponse(request)
    update = super_admin.objects.get(id=id)
    if request.method == "POST":
        update.name = request.POST["name"]
        update.email = request.POST["email"]
        update.password = base64.b64encode(bytes(request.POST["password"], "utf-8")).decode()
        update.company = request.POST["company"]
        update.address = request.POST["address"]
        update.phone = request.POST["phone"]
        update.website = request.POST["website"]
        update.type = request.POST["type"]
        if len(request.FILES) != 0:
            if len(update.avatar) > 0:
                os.remove(update.avatar.path)
            update.avatar = request.FILES['avatar']
        update.save()
        return redirect('user-admin')

    context = {'update':update}
    return render(request, 'products/edit.html', context)
    #     return redirect("user-admin")
    # else:
    #     return render(request, "admin_user/page/useradmin/edit.html", {"update": update})
    
def user_admin_delete(request, id):
    update = super_admin.objects.get(id=id)
    if len(update.avatar) > 0:
        os.remove(update.avatar.path)
 
    update.delete()
    return redirect("user-admin")