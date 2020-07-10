from django.conf.urls import url
from django.urls import path
from . import views

app_name = "waitinglist"

urlpatterns = [
    path('', views.NewUserView, name='waitinglistindex')
]