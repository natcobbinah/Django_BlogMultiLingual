from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/chatbot/room/', consumers.Chatconsumer.as_asgi(),)
]
