from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from meals import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
)
