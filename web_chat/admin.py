from django.contrib import admin
from .models import *

@admin.register(Message)
class Admin(admin.ModelAdmin):
    pass
    list_display = ('id','content', 'user', 'created_at')#, 'chat_room')
    #list_filter = ('is_completed',)	      		      
    #search_fields = ('title',) 			      
    #fields = ("id", "title") 
    

@admin.register(ChatRoom)
class Admin(admin.ModelAdmin):
    list_display = ('title','created_at', 'updated_at',)

@admin.register(ChatUser)
class Admin(admin.ModelAdmin):
    list_display = ['auth_token', 'id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']#]