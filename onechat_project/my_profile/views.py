from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy


class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my_profile:profile')


@login_required
def profile(request):
    return render(request, 'my_profile/profile.html')
