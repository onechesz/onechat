from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import PrivateMessage


@login_required
def user(request, username: str):
    if request.user.username == username:
        return redirect('my_profile:profile')

    user_data = User.objects.get(username=username)
    current_user = request.user
    messages = PrivateMessage.objects.filter(
        (Q(receiver=user_data.username) | Q(receiver=current_user.username)),
        (Q(sender=user_data.username) | Q(sender=current_user.username))).order_by('-date_added')[:20][::-1]

    return render(request, 'user/user.html', {
        'user_data': user_data,
        'messages': messages,
        'current_user': current_user
    })
