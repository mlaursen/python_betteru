import datetime, re

from django import forms
from django.forms import ModelForm, Form
from django.forms.util import ErrorList
from django.utils.timezone import utc


from accounts.models import TempAccount, Account, AccountSettings
from utils.util import valid_user, createcode, create_birthday_time, birthday_time_as_str, in_ttuple

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

    def is_valid(self):
        valid = super(EditAccountForm, self).is_valid()
        GENDERS = Account.GENDER_CHOICES[1:]
        UNITS = Account.UNIT_CHOICES[1:]
        birthday = birthday_time_as_str(self.cleaned_data.get('birthday'))
        gender = self.cleaned_data.get('gender')
        units = self.cleaned_data.get('units')

        if not in_ttuple(GENDERS, gender):# not in GENDERS:
            self._errors['gender_errs'] = ErrorList([u"You must select a gender."])
            valid = False

        if units not in UNITS:
            self._errors['units_errs'] = ErrorList([u"You must select a unit."])
            valid = False

        #if mult not in MULTIPLIERS:
        #    self._errors['multipliers_errs'] = ErrorList([u"A valid multiplier must be selected."])
        #    valid = False

        if not re.findall('^\d\d/\d\d/\d\d\d\d', birthday):
            self._errors['birthday'] = ErrorList([u"Invalid birthday.  The correct format is (mm/dd/yyyy)."])
            valid = False

        #if not isinstance(height, (int)):
        #    self._errors['height'] = ErrorList([u"The height must be a number in inches or centimeters"])
         #   valid = False


        return valid

    class Meta:
        model = Account
        fields = ['birthday', 'gender', 'units'] #, 'activity_multiplier']
        widgets = { 
            'birthday': forms.DateInput(format=('%m/%d/%Y'),
                                        attrs={'placeholder': 'Select a date',
                                               'maxlength': 10,},),
            #'height': forms.TextInput(attrs={'placeholder': 'Enter your height'},),
    }



class EditAccountSettingsForm(ModelForm):
    def is_valid(self):
        valid = super(EditAccountSettingsForm, self).is_valid()
        RECALC = AccountSettings.DOW_CHOICES[1:]
        MULTIPLIERS = AccountSettings.MULTIPLIER_CHOICES[1:]

        return valid

    class Meta:
        model = AccountSettings
        fields = ['recalculate_day_of_week', 'height', 'activity_multiplier']
        widgets = {
            'height': forms.TextInput(attrs={'placeholder': 'Enter your height'},),
            #'recalculate_day_of_week': forms.TextInput(attrs={'placeholder': 'Enter the day you want to recalculate TDEE'},),
        }
        


