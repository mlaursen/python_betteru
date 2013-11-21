from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from goals import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/meal_(?P<meal_id>\d+)$', views.add, name='add'),
)
