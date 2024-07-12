from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Register(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    mobile = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=50, null=False) 
    re_renter_password = models.CharField(max_length=50,null=False) 
    
    #models.EmailField(_(""), max_length=254)
    def __str__(self):
        return self.user.email