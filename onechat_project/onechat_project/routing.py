from django.urls import path

from rooms import consumers as rooms_consumers
from user import consumers as user_consumers

websocket_urlpatterns = [
    path('ws/<str:sender>-<str:receiver>/', user_consumers.ChatConsumer.as_asgi()),
    path('ws/<str:room_name>/', rooms_consumers.ChatConsumer.as_asgi())
]
