import datetime, re

from django import forms
from django.forms import ModelForm, Form
from django.forms.util import ErrorList
from django.utils.timezone import utc


from accounts.models import TempAccount, Account
from utils.util import valid_user, createcode, create_birthday_time, birthday_time_as_str

def gender_choices():
    GENDER_CHOICES = (
            ('select_gender', 'Select Gender'),
            ('m', 'Male'),
            ('f', 'Female'),
    )
    return GENDER_CHOICES

def unit_choices():
    UNIT_CHOICES = (
            ('select_units', 'Select Units'),
            ('imperial', 'Imperial'),
            ('metric', 'Metric'),
    )
    return UNIT_CHOICES

def multiplier_choices():
    MULTIPLIERS = (
            ('select_multiplier', 'Select Activity Multiplier'),
            ('sedentary', 'Sedentary - 1.2'),
            ('lightly', 'Lightly Active - 1.375'),
            ('moderately', 'Moderately Active - 1.55'),
            ('very', 'Very Active - 1.725'),
            ('extremely','Extremely Active - 1.9'),
    )
    return MULTIPLIERS

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
        cuser = self.cleaned_data.get('username')
        cpswd = self.cleaned_data.get('password')

        if not valid or not valid_user(cuser, cpswd):
            self._errors['invalid_login'] = ErrorList([u"Invalid username or password."])
            valid = False

        return valid

class EditAccountForm(ModelForm):
    gender = forms.ChoiceField(choices=gender_choices())
    units = forms.ChoiceField(choices=unit_choices())
    multipliers = forms.ChoiceField(choices=multiplier_choices())

    def is_valid(self):
        valid = super(EditAccountForm, self).is_valid()
        MULTIPLIERS = ('sedentary', 'lightly', 'moderately', 'very', 'extremely')
        mult = self.cleaned_data.get('multipliers')
        birthday = birthday_time_as_str(self.cleaned_data.get('birthday'))
        height = self.cleaned_data.get('height')

        if mult not in MULTIPLIERS:
            e1 = u"A valid multiplier must be selected. %s is not valid" % mult
            self._errors['multipliers'] = ErrorList([e1])
            valid = False

        if not re.findall('^\d\d/\d\d/\d\d\d\d', birthday):
            self._errors['birthday'] = ErrorList([u"Invalid birthday.  The correct format is (mm/dd/yyyy)."])
            valid = False

        if not isinstance(height, (int)):
            self._errors['height'] = ErrorList([u"The height must be a number in inches or centimeters"])
            valid = False


        return valid

    class Meta:
        model = Account
        fields = ['birthday', 'height']
        widgets = { 
            'birthday': forms.DateInput(format=('%m/%d/%Y'),
                                        attrs={'placeholder': 'Select a date'}),
            'height': forms.TextInput(attrs={'placeholder': 'Enter your height'},)
    }


