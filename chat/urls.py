from django.urls import path
from .views import  chat_view


urlpatterns = [
    # path('', chat_ui, name='chat-ui'),
    path("api/chat/", chat_view, name="chat"),
    # path('api/chat/', ChatAPIView.as_view(), name='chat-api'),

]
