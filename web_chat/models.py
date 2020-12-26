from django.db import models
from django.contrib.auth.models import AbstractUser

class ChatUser(AbstractUser):
    is_active = models.BooleanField(default=True)
    last_room_create = models.DateTimeField(null=True)
    pass


class Message(models.Model):
    content = models.TextField(blank=False, verbose_name='Message_text')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created:')
    user = models.ForeignKey(ChatUser, on_delete=models.PROTECT, blank=False, verbose_name="User", default=1)
    chat_room = models.ForeignKey("ChatRoom", on_delete=models.CASCADE, blank=False, verbose_name=("Chat_room"))
    def __str__(self):
        return self.content[:20]

class ChatRoom(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title', blank=False)
    user = models.ForeignKey(ChatUser, on_delete=models.PROTECT, blank=False, verbose_name="User", default=1)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title