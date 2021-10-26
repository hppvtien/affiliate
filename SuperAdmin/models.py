from django.db import models
import requests
from django.db import connection
import json
from core import settings
import base64
import datetime
import os

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class super_admin(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    company = models.TextField(null=True)
    address = models.TextField()
    website = models.TextField(null=True)
    phone = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    avatar = models.ImageField(null=True, blank=True, upload_to=filepath)
    