from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

from accounts.models import TempAccount, Account, valid_user, createcode, send_confirmation_email
from accounts.forms import CreateForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.core.urlresolvers import reverse


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

#class CreateAccountView(FormView):
#    template_name = 'accounts/create.html'
#    form_class = CreateForm
#    success_url = '/'

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
    if request.method == 'POST':
        f = CreateForm(request.POST)
        if f.is_valid():
            user = f.cleaned_data['username']
            pswd = f.cleaned_data['password']
            email = f.cleaned_data['email']
            code = createcode()
            TempAccount.objects.create_tempaccount(user, pswd, email, code)
            if send_confirmation_email(email, code):
                msg = {'pagename': 'Email Sent',
                        'message': 'An email confirmation has been sent to ' + email,
                        'location': '/',
                        'success': True,
                        'time': 3
                }
            else:
                msg = {'pagename': 'Email Failure',
                        'location': reverse('accounts:create'),
                        'time': 3,
                        'message': 'Something went wrong when attempting to send an email. Please try again.',
                }
            return render(request, 'redirect.html', {'msg': msg})
    else:
        f = CreateForm()

    return render(request, 'accounts/create.html', {'form': f,})


def confirm(request):
    conf = {'pagename': 'Confirm Email', 
            'message': 'You have successfully confirmed your email.  Redirecting in 3 seconds.',
            'location': '/',
            'success': True,
            'time': 3,
    }
    errs = {'pagename': 'Invalid Email Confirmation',
            'message': 'The email confirmation link is invalid.  Please try to copy the link again.',
    }
    code = request.GET.get('code')
    email = request.GET.get('email')
    if code is not None and email is not None and TempAccount.objects.filter(code=code, email=email).exists():
        t = TempAccount.objects.get(code=code, email=email)
        Account.objects.create_account_from_temp(t)
        t.delete()
        return render(request, 'redirect.html', {'msg': conf})
    else:
        return render(request, 'errorpage.html', {'msg': errs})


