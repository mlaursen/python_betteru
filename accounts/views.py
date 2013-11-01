from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from accounts.models import TempAccount, Account
from utils.util import Redirect, ErrorPage, valid_user, createcode, send_confirmation_email
from accounts.forms import CreateForm, LoginForm, EditAccountForm


def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            cuser = f.cleaned_data.get('username')
            cpass = f.cleaned_data.get('password')
            if valid_user(cuser, cpass):
                a = Account.objects.get(username=cuser)
                request.session['uid'] = a.id
                return HttpResponseRedirect(reverse('accounts:index'))
    else:
        f = LoginForm()
    return render(request,
            'accounts/login.html',
            {'form': f, 'create_form': CreateForm()}
    )

def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return Redirect('Logged Out', 'You have successfully logged out.').redirect(request)


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
                r = Redirect('Email Sent', "An email confirmation has been sent to %s." % email)
            else:
                r = Redirect('Email Failure',
                        'Something went wrong when attempting to send an email. Please try again.',
                        reverse('accounts:create'),
                        'failure'
                )
            return r.redirect(request)
    else:
        f = CreateForm()

    return render(request, 'accounts/create.html', {'create_form': f,})


def confirm(request):
    conf = {'pagename': 'Confirm Email', 
            'message': 'You have successfully confirmed your email!  Redirecting to login page in 3 seconds.',
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
        return Redirect('Confirm Email', 'You have successfully confirmed your email!  ').redirect(request)
    else:
        return ErrorPage('Invalid Email Confirmation', 'The email confirmation link is invalid.  Please try to copy the link again.').send(request)


def edit(request):
    if request.method == 'POST':
        f = EditAccountForm(request.POST)
    else:
        f = EditAccountForm()

    return render(request,'accounts/edit.html', {'edit_account_form': f})
