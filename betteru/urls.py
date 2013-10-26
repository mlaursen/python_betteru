from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="info.html")),

    url(r'^stats/',         include('stats.urls',       namespace="stats")),
    url(r'^accounts/',      include('accounts.urls',    namespace="accounts")),
    url(r'^ingredients/',   include('ingredients.urls', namespace="ingredients")),
    url(r'^meals/',         include('meals.urls',       namespace="meals")),
    url(r'^goals/',         include('goals.urls',       namespace="goals")),
)
