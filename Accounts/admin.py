from django.contrib import admin
from .models import Register 
# Register your models here.
@admin.register(Register)
class Studentmodel(admin.ModelAdmin): 
    list_display=['id','name','email'] 
    