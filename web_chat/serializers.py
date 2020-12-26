from rest_framework import serializers
from .models import ChatRoom, Message, ChatUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUser
        fields = ['username', 'password', 'is_active', 'first_name']
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = ChatUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class MessageSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Message
        fields = '__all__'

class ChatroomSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = ChatRoom
        fields = ['id', 'title', 'created_at', 'updated_at', 'username']

