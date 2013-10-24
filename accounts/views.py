from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from accounts.models import Account


class IndexView(generic.base.TemplateView):
    template_name = 'accounts/index.html'

def login(request):
    a = Account.objects.get(id=request.POST['id'])
    if a.password == request.POST['password']:
        request.session['uid'] = a.id
        return HttpResponse("You're logged in.")
    else:
        return HttpRespnse("Your username and password didn't match")

def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
