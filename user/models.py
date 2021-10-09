from django.db import models
from django.contrib.auth.models import User, auth
from allauth.socialaccount.models import SocialApp, SocialToken
import requests
from django.db import connection
import json


class user_profile(models.Model):
    profile_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='/image/helen.jpg')
    address = models.TextField()
    phone = models.CharField(max_length=50)
    


    def get_token_id(account_id):
        get_token = SocialToken.objects.only('token').filter(account_id = account_id)
        return get_token
    
    def get_token_twitter(provider):
        get_token = SocialApp.objects.only('client_id', 'secret').filter(provider = provider)
        return get_token
    
    def get_token_app_accounts_user_logded(user_logged_accounts):
        cursor = connection.cursor()
        cursor.execute("SELECT socialaccount_socialaccount.provider, socialaccount_socialaccount.id, socialaccount_socialtoken.token FROM socialaccount_socialaccount JOIN socialaccount_socialtoken ON socialaccount_socialaccount.id = socialaccount_socialtoken.account_id WHERE user_id =" + str(user_logged_accounts))
        data1 = cursor.fetchall()
        
        return data1
    
class share_link(models.Model):
    name = models.TextField()
    code = models.TextField(unique=True)
    code_invite = models.TextField(unique=True)
    by_invite = models.TextField(default='No invite')
    address = models.TextField()
    phone = models.CharField(max_length=50)


class share_link_page(models.Model):
    user_id = models.IntegerField()
    code = models.TextField()
    page_link = models.TextField()
    count_view_site = models.IntegerField()

    
    


