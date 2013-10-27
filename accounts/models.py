from django.shortcuts import render
from django.utils import timezone
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db import models

import hashlib, uuid


class AccountManager(models.Manager):
    def create_full_account(self, user, pswd, bday, gender, units, height, act_mult, email):
        h = createhash(user, pswd)
        account = self.create(username=user,
                password=h,
                birthday=bday,
                gender=gender,
                units=units,
                height=height,
                activity_multiplier=act_mult,
                email=email,
                active_since=timezone.now()
        )
        return account

    def create_account_from_temp(self, tmp):
        account = self.create(username=tmp.username,
                password=tmp.password,
                email=tmp.email,
                active_since=timezone.now()
        )
        del tmp
        return account


class Account(models.Model):
    id       = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    birthday = models.DateTimeField('birthday')
    gender   = models.CharField(max_length=1)
    units    = models.CharField(max_length=8)
    height   = models.IntegerField()
    activity_multiplier = models.CharField(max_length=30)
    email    = models.CharField(max_length=40)
    active_since = models.DateTimeField('active since')

    objects = AccountManager()

    def __str__(self):
        str = "user: " + self.username + "\n"
        str += "units: " + self.units + "\n"
        str += "email: " + self.email + "\n"
        return str


class TempAccountManager(models.Manager):
    def create_tempaccount(self, user, pswd, email, code):
        h = createhash(user, pswd)
        tmp = self.create(username=user, password=h, email=email, code=code, creation=timezone.now())
        return tmp




class TempAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    email    = models.CharField(max_length=40)
    code     = models.CharField(max_length=32)
    creation = models.DateTimeField('create date')

    objects = TempAccountManager()

    def __str__(self):
        str  = "user: " + self.username + "\n"
        str += "email: " + self.email + "\n"
        str += "code: " + self.code + "\n"
        return str



def send_confirmation_email(email, code):
    subject = "BetterU Email Confirmation"
    message = "Thanks for signing up for BetterU.  Please follow the link below.\n"
    message += "http://localhost:8000" + reverse('accounts:confirm') + "?code=" + code + "&email=" + email
    email_to_send = EmailMessage(subject, message, to=[email,])
    return email_to_send.send()


def createcode():
    return str(uuid.uuid1().hex)



def createhash(user, pswd):
    ran = str(uuid.uuid4().hex)
    salt = hashlib.sha256( str( ran + "super secret PassTHingy herr" + user ).encode('utf-8') ).hexdigest()
    return repeated_hashing(salt, pswd)


def repeated_hashing(salt, pswd):
    h = salt + pswd
    for i in range(0, 10000):
        h = str( hashlib.sha256(h.encode('utf-8')).hexdigest() )

    return salt + h


def valid_user(user, pswd):
    try:
        a = Account.objects.get(username=user)
        salt = a.password[:64]
        h = repeated_hashing(salt, pswd)
        return h == a.password
    except:
        return False

def logged_in(request):
    return 'uid' in request.session


class Redirect(object):
    msg = {}
    def redirect(self, request):
        return render(request, 'redirect.html', {'msg': self.msg})

    def __str__(self):
        return str(self.msg)

    def __init__(self, pname, message, loc=False, type='success', time=3):
        if not loc:
            message += "Redirecting to the login page in %s seconds." % time
            loc = '/'
        msg = {'pagename': pname,
            'message': message,
            'location': loc,
            'type': type,
            'time': time,
        }
        self.msg = msg



