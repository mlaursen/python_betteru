from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.utils import timezone

class IndexView(TemplateView):
    template_name = 'goals/index.html'

