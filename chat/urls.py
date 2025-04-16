from django.urls import path
from .views import ChatAPIView, chat_ui


urlpatterns = [
    path('', chat_ui, name='chat-ui'),
    path('api/chat/', ChatAPIView.as_view(), name='chat-api'),
]
