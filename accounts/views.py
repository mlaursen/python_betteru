from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from accounts.models import Account, valid_user


class IndexView(generic.base.TemplateView):
    template_name = 'accounts/index.html'

class LoginView(generic.base.TemplateView):
    template_name = 'accounts/login.html'

class CreateAccountView(generic.base.TemplateView):
    template_name = 'accounts/create.html'


def login(request):
    user = request.POST['username']
    pswd = request.POST['password']
    a = get_object_or_404(Account, username=user)

    if valid_user(user, pswd):
        request.session['uid'] = a.id
        return HttpResponseRedirect(reverse('accounts:index') + "?msg=Woo!")
    else:
        return HttpResponseRedirect('/login/?msg=Booooo')

def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

