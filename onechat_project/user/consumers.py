import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from .models import PrivateMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender = self.scope['url_route']['kwargs']['sender']
        self.receiver = self.scope['url_route']['kwargs']['receiver']

        if self.sender > self.receiver:
            self.group = self.sender + '-' + self.receiver
        else:
            self.group = self.receiver + '-' + self.sender
        self.room_group_name = 'chat_%s' % self.group

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        date = data['date']
        message = data['message']
        sender = data['sender']
        receiver = data['receiver']

        await self.save_message(sender, receiver, message)

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'date': date,
            'message': message,
            'sender': sender,
            'receiver': receiver
        })

    async def chat_message(self, event):
        date = event['date']
        message = event['message']
        sender = event['sender']
        receiver = event['receiver']

        await self.send(text_data=json.dumps({
            'date': date,
            'message': message,
            'sender': sender,
            'receiver': receiver
        }))

    @sync_to_async
    def save_message(self, sender, receiver, message):
        user = User.objects.get(username=sender)
        receiver = User.objects.get(username=receiver)

        PrivateMessage.objects.create(sender=sender, receiver=receiver, content=message)
