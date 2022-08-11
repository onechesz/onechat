from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def index(request):
    return render(request, 'core/index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('core:index')
    else:
        form = SignUpForm()

    return render(request, 'core/sign_up.html', {'form': form})
