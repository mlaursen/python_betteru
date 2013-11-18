from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from meals.models import *

class IndexView(generic.base.TemplateView):
    template_name = 'meals/index.html'

class AddView(generic.base.TemplateView):
    template_name = 'meals/add.html'

def index(request):
    meals = MealView.objects.all()
    return render(request, 'meals/index.html', {'meals': meals,})

