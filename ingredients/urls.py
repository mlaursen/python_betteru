from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from ingredients import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    #url(r'^add/$', views.AddView.as_view(), name='add'),
)
