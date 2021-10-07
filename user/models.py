from django.db import models
from django.contrib.auth.models import User, auth
from allauth.socialaccount.models import SocialApp, SocialToken
import requests


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
        
class share_link(models.Model):
    user_id = models.TextField()
    name = models.TextField()
    code = models.TextField(unique=True)
    address = models.TextField()
    count_view_site = models.IntegerField(default=0)
    phone = models.CharField(max_length=50)
class share_link_page(models.Model):
    user_id = models.IntegerField()
    page_link = models.TextField()
    count_view_site = models.IntegerField(default=0)
    created_at = models.DateField()
    
    

    
    


