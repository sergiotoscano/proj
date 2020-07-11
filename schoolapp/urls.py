from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'schoolapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='indexschoolapp'),
    path('list', views.SchoolListView.as_view(), name='schoollist'),
    re_path(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='schooldetail'),
    path('create', views.SchoolCreateView.as_view(), name='schoolcreate'),
    re_path(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='schoolupdate'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='schooldelete'),
]
