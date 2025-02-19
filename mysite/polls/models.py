import datetime

from django.db import models
from django.utils import timezone
from django.db import models




class SibTransUser(models.Model):
    title= models.CharField(max_length=200,default="")
    cr2d = models.DateTimeField()
   