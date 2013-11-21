from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.utils import timezone

from goals.models import *
from accounts.models import Account
from utils.util import logged_in

class IndexView(TemplateView):
    template_name = 'goals/index.html'

def add(request, meal_id):
    """
    Adds a meal to the current day and user
    Will need to check if logged in
    """
    return render(request, 'goals/index.html', {'mid': meal_id,})

def index(request):
    if logged_in(request):
        a = Account.objects.get(pk=request.session.get('uid'))
    else:
        a = Account.objjects.get(pk=1)
    goals = Goal.objects.filter(account=a)
    return render(request, 'goals/index.html', {'goals': goals,})

