from django.db import models

# Create your models here.
class Request(models.Model):
    Name              =models.CharField(max_length=80)
    Username          =models.CharField(max_length=20)
    Email             =models.EmailField()
    Department        =models.CharField(max_length=20)
    Project           =models.CharField(max_length=40)
    Manager           =models.CharField(max_length=80)
    Justification     =models.TextField()
    StartDate         =models.DateField()
    AccessDuration    =models.AutoField()
    S3Bucket       =models.CharField(max_length=80)
    Permission   =models.CharField(max_length=20, default='Read/Write')
