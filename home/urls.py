from django.conf.urls import url
from django.urls import path
from home import views


#TEMPLATE TAGGING
app_name = 'home'

urlpatterns = [
    path('', views.homeview, name='homeindex'),
    path('home/base/', views.baseview, name='baseview')
]
