from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from accounts.models import TempAccount, Account, AccountSettings, AccountSettingsView
from utils.util import Redirect, ErrorPage, valid_user, createcode, send_confirmation_email
from accounts.forms import CreateForm, LoginForm, EditAccountSettingsForm, EditAccountForm 
from datetime import date


def login(request):
    """
    Handles a user trying to log in.
    """
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            cuser = f.cleaned_data.get('username')
            cpass = f.cleaned_data.get('password')
            if valid_user(cuser, cpass):
                a = Account.objects.get(username=cuser)
                request.session['uid'] = a.id
                if a.settings_complete():
                    return HttpResponseRedirect(reverse('stats:index'))
                else:
                    return HttpResponseRedirect(reverse('accounts:index'))
    else:
        f = LoginForm()
    return render(request,
            'accounts/login.html',
            {'form': f, 'create_form': CreateForm()}
    )


def logout(request):
    """
    Handles the user trying to log out.  Deletes the session for the user and redirec tto the index page
    """
    try:
        del request.session['uid']
    except KeyError:
        pass
    return Redirect('Logged Out', 'You have successfully logged out.').redirect(request)


def index(request):
    example = Account.objects.get(pk=0)
    disable = False
    if request.session.has_key('uid'):
        a = get_object_or_404(Account, pk=request.session['uid'])
    else:
        a = example
        disable = True


    success=False

    if request.method == 'POST' and a != example:
        f = EditAccountForm(request.POST)
        f2 = EditAccountSettingsForm(request.POST)
        if f.is_valid() and f2.is_valid():
            bday = f.cleaned_data.get('birthday')
            gender = f.cleaned_data.get('gender')
            units = f.cleaned_data.get('units')
            height = f2.cleaned_data.get('height')
            mult   = f2.cleaned_data.get('activity_multiplier')
            recalc = f2.cleaned_data.get('recalculate_day_of_week')
            a.birthday = bday
            a.gender = gender
            a.units = units
            a.save()
            if AccountSettings.objects.filter(account=a, date_changed=date.today):
                acts = AccountSettings.update_account_settings(a, date.today, recalc, mult, height)
            else:
                acts = AccountSettings.objects.create_account_settings(a, recalc, height, mult)
                acts.save()
            success = 'You have successfully updated your account information!'
    else:
        f = EditAccountForm(instance=a)
        account_settings = AccountSettings.objects.filter(account=a)
        if account_settings:
            account_settings = get_object_or_404(AccountSettingsView, account=a)
            f2 = EditAccountSettingsForm(instance=account_settings)
        else:
            f2 = EditAccountSettingsForm()

    return render(request,'accounts/index.html', {'form': f,
        'settings': f2,
        'account': a,
        'success': success,
        'disable': disable,
        })


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


def confirm_email(request):
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


