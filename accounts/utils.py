from django.utils import timezone
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse

from accounts.models import Account

import hashlib, uuid

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

    def __str__(self):
        return str(self.msg)


    def __init__(self, pname, message, loc='/', divtype='success', login=True, time=3):
        if login:
            message += " Redirecting to the login page in %s seconds." % time
        msg = {'pagename': pname,
                'message': message,
                'location': loc,
                'time': time,
                'type': divtype,
        }
        self.msg = msg
