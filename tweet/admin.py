from django.contrib import admin
from .models import *
# Register your models here.

 
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user','text','photo','created_at','updated_at')

admin.site.register(Tweet, TweetAdmin)
