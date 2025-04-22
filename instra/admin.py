from django.contrib import admin

# Register your models here.

from .models import *

class ShowRegisterData(admin.ModelAdmin):
    list_display = ["id","name","email","username","password"]

admin.site.register(UserRegister,ShowRegisterData)

class ShowPosts(admin.ModelAdmin):
    list_display = ["id","nameuser","post_photos","description","date"]

admin.site.register(PosttModel,ShowPosts)
