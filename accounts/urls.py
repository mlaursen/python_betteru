from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from accounts import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.CreateAccountView.as_view(), name='create'),
    #url(r'^confirm/$', views.ConfirmAccountView.as_view(), name='confirm'),
    url(r'^confirm/$', views.confirm, name='confirm'),
)
