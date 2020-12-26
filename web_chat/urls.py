from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

urlpatterns = [
    path('api/messages-by-room/<int:cat>/', RoomMessagesList.as_view()),
    path('api/messages/<int:pk>/', MessageDetail.as_view()),
    path('api/messages/', MessageList.as_view()),
    path('api/chatrooms/', ChatRoomView.as_view()), 
    path('api/chatrooms/<int:pk>/', ChatRoomDetail.as_view()), 
    path('api/auth/create/', CreateUser.as_view()),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/logout/', LogoutUser.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
    path('api/auth/check/', TokenVerifyView.as_view()),
    path('api/auth/user/', GetUserData.as_view()),
]

