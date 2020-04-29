from django.db import models
from hashlib import md5
from datetime import datetime

# Create your models here.
class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Click(models.Model):
    url_hash =  models.ForeignKey(URL,on_delete=models.SET_NULL,null=True,blank=True)
    timestamp = models.DateTimeField(default=datetime.now)
        