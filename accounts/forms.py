from django import forms
from django.forms import ModelForm, Form
from accounts.models import TempAccount, createcode
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList

from accounts.models import TempAccount, Account

class CreateForm(ModelForm):
    password_confirm = forms.CharField(max_length=128,
            min_length=8,
            widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password = forms.CharField(max_length=128,
            min_length=8,
            widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def is_valid(self):
        valid = super(CreateForm, self).is_valid()

        email = self.cleaned_data.get('email')
        if TempAccount.objects.filter(email=email).exists():
            self._errors['check_email'] = ErrorList([u"You already have an account waiting to be verified for this email address.",
                u"Please check your inbox for a confirmation from betteru.webmaster@gmail.com"])
            self._errors['email'] = ErrorList([u"Email already exists."])
            valid = False

        if Account.objects.filter(email=email).exists():
            self._errors['account_exists'] = ErrorList([u"You already have an account with this email.  Please log in with that account.",
                u"If you can not remember the account name, click the Forgot Account/Password link on the login page."])
            self._errors['email'] = ErrorList([u"Email already exists."])
            valid = False

        if self.cleaned_data.get('password') != self.cleaned_data.get('password_confirm'):
            self._errors['password'] = ErrorList([u"Passwords must match."])
            self._errors['password_confirm'] = ErrorList([u"Passwords must match."])
            valid = False

        return valid

    class Meta:
        model = TempAccount
        fields = ['username', 'password', 'email']
        widgets = { 
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }

class LoginForm(Form):
    username = forms.CharField(max_length=40,
            widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(max_length=128,
            min_length=8,
            widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        user = self.cleaned_data.get('username')
        pswd = self.cleaned_data.get('password')

        if not Account.objects.filter(username=user, password=pswd).exists() or not valid:
            self._errors['invalid_login'] = ErrorList([u"Invalid username or password."])
            valid = False

        return valid

