from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from accounts import views

urlpatterns = patterns('',
    url(r'^settings/$', views.index, name='index'),
    url(r'^create/$', views.create_temp, name='create'),
    url(r'^confirm/$', views.confirm, name='confirm'),
    url(r'^login/$', views.login, name='login'),
)
