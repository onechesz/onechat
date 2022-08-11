from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message


@login_required
def rooms(request):
    room_list = Room.objects.all

    return render(request, 'rooms/rooms.html', {'room_list': room_list})


@login_required
def room(request, slug):
    room_info = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room_info)[0:25]

    return render(request, 'rooms/room.html', {
        'room_info': room_info,
        'messages': messages
    })
