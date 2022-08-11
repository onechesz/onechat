from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out/', LogoutView.as_view(), name='log_out'),
    path('log_in/', LoginView.as_view(template_name='core/log_in.html'), name='log_in')
]
