from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from accounts.models import TempAccount, Account, valid_user, createcode
from accounts.forms import CreateForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

class CreateAccountView(FormView):
    template_name = 'accounts/create.html'
    form_class = CreateForm
    success_url = '/'

def login(request):
    user = request.POST['username']
    pswd = request.POST['password']
    a = get_object_or_404(Account, username=user)

    if valid_user(user, pswd):
        request.session['uid'] = a.id
        return HttpResponseRedirect(reverse('accounts:index'))
    else:
        return HttpResponseRedirect('/login/')

def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def index(request):
    if request.session.has_key('uid'):
        a = get_object_or_404(Account, pk=request.session['uid'])
    else:
        a = Account.objects.get(pk=0)
    return render(request, 'accounts/index.html', {'account': a})

def create_temp(request):
    user = request.POST['username']
    pswd = request.POST['password']
    if TempAccount.objects.filter(username=user).exists():
        return HttpResponseRedirect('accounts:create')
    else:
        t = TempAccount.objects.create_tempaccount(user, paswd, createcode())
        t.save()
        return HttpResponseRedirect(reverse('accounts:index'))

def confirm(request):
    conf = {'pagename': 'Confirm Email', 
            'message': 'You have successfully confirmed your email.  Redirecting in 3 seconds.',
            'time': '2000',
    }
    errs = {'pagename': 'Invalid Email Confirmation',
            'message': 'The email confirmation link is invalid.  Please try to copy the link again.',
    }
    code = request.GET.get('code')
    email = request.GET.get('email')
    if code is not None and email is not None and TempAccount.objects.filter(code=code, email=email).exists():
        return render(request, 'redirect.html', {'msg': conf})
    else:
        return render(request, 'errorpage.html', {'msg': errs})


