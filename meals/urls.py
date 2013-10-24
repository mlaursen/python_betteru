from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from meals import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.AddView.as_view(), name='add'),
)
