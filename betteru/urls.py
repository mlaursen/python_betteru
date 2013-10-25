from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^info/$', TemplateView.as_view(template_name="info.html")),
    url(r'^stats/', include('stats.urls', namespace="stats")),
    url(r'^accounts/login/', 'accounts.views.login', name="login"),
    url(r'^logout/', 'accounts.views.logout', name="logout"),
    url(r'^settings/', include('accounts.urls', namespace="accounts")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^ingredients/', include('ingredients.urls', namespace="ingredients")),
    url(r'^meals/', include('meals.urls', namespace="meals")),
    url(r'^goals/', include('goals.urls', namespace="goals")),
    # Examples:
    # url(r'^$', 'betteru.views.home', name='home'),
    # url(r'^betteru/', include('betteru.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
