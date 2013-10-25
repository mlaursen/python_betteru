from django import forms
from django.forms import ModelForm
from accounts.models import TempAccount, createcode
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList

class CreateForm(ModelForm):
    password_confirm = forms.CharField(max_length=128,
            min_length=8,
            widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password = forms.CharField(max_length=128,
            min_length=8,
            widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_confirm'):
            self._errors['password'] = ErrorList([u"Passwords must match."])
            self._errors['password_confirm'] = ErrorList([u"Passwords must match."])
        return self.cleaned_data


    class Meta:
        model = TempAccount
        fields = ['username', 'password', 'email']
        widgets = { 
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }


    def create_temp(self):
        code = createcode()
        TempAccount.objects.create_tempaccount(self.username, self.password, self.email, code)
        pass

