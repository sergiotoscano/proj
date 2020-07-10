from django.conf.urls import url
from django.urls import path
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='indexfirstapp'),
    path('formpage/', views.form_name_view, name='formfirstapp')
]
