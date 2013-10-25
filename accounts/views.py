from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from accounts.models import Account


class IndexView(generic.base.TemplateView):
    template_name = 'accounts/index.html'

class LoginView(generic.base.TemplateView):
    template_name = 'accounts/login.html'

class CreateAccountView(generic.base.TemplateView):
    template_name = 'accounts/create.html'


def login(request):
    a = get_object_or_404(Account, username=request.POST['username'])
    if a.password == request.POST['password']:
        request.session['uid'] = a.id
        return HttpResponseRedirect(reverse('accounts:index'))
    else:
        str = "Invalid username or password: " + a.username + ", " + a.password
        return HttpResponse(str)

def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('accounts:index'))

