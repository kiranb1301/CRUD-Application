from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    mobile = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=50, null=False) 
    re_renter_password = models.CharField(max_length=50,null=False)