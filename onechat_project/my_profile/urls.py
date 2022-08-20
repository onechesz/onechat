from django.contrib.auth.views import PasswordChangeView
from django.urls import path, reverse

from . import views

app_name = 'my_profile'
urlpatterns = [
    path('', views.MyPasswordChangeView.as_view(template_name='my_profile/profile.html'), name='profile')
]
