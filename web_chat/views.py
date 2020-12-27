from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import *
from django.utils import timezone
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateUser(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_active = True)
        return Response({"success":"user {} is created".format(serializer.validated_data['username'])}, status=status.HTTP_201_CREATED)

class MessageList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            room = ChatRoom.objects.get(pk=serializer.data['chat_room'])
            room.updated_at = timezone.now()
            room.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        message = self.get_object(pk)
        if (request.user == message.user or request.user.is_staff or request.user.is_superuser):
            message.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class RoomMessagesList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, cat):
        queryset = Message.objects.filter(chat_room = cat)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

class ChatRoomView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        queryset = ChatRoom.objects.all()
        serializer = ChatroomSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatroomSerializer(data=request.data)
        if serializer.is_valid():
            last_created = request.user.last_room_create
            serializer.save(user = request.user)
            user = request.user
            user.last_room_create = timezone.now()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatRoomDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, pk):
        try:
            return ChatRoom.objects.get(pk=pk)
        except ChatRoom.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        ChatRoom = self.get_object(pk)
        if (request.user == ChatRoom.user or request.user.is_staff or request.user.is_superuser):
            ChatRoom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class GetUserData(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        username = request.user.username
        user = request.user
        perms = ""
        if user.is_superuser:
            perms = "staff"
        elif user.is_staff:
            perms = "super"
        else:
            perms = "user"
            
        return Response({"username":username, "permissions": perms})
