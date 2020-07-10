from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [
    path('', views.register, name='registerauthapp'),
    path('login/', views.user_login, name='loginauthapp'),
    path('logout/', views.user_logout, name='logoutauthapp'),
]   
