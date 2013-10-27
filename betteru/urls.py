from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from betteru import views

urlpatterns = patterns('',
    url(r'^$',              RedirectView.as_view(url='/accounts/login/', permanent=False), name="index"), 
    url(r'^info/$',         views.info, name="info"), 
    url(r'^stats/',         include('stats.urls',       namespace="stats")),
    url(r'^accounts/',      include('accounts.urls',    namespace="accounts")),
    url(r'^ingredients/',   include('ingredients.urls', namespace="ingredients")),
    url(r'^meals/',         include('meals.urls',       namespace="meals")),
    url(r'^goals/',         include('goals.urls',       namespace="goals")),
    url(r'^.*$',            TemplateView.as_view(template_name='404.html'), name='404'),
)
