from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from stats.models import Stats

class IndexView(generic.base.TemplateView):
    template_name = 'stats/index.html'

