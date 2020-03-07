from django.contrib import admin
from login.models import *
# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ['user','image']
admin.site.register(Profile,AdminProfile)
