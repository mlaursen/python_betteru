from django.db import models
import hashlib, uuid
from django.utils import timezone

# Create your models here.
class AccountManager(models.Manager):
    def create_account(self, user, pswd, bday, gender, units, height, act_mult, email):
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




class TempAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    email    = models.CharField(max_length=40)
    code     = models.CharField(max_length=32)
    creation = models.DateTimeField('create date')

    def __str__(self):
        str  = "user: " + self.username + "\n"
        str += "email: " + self.email + "\n"
        str += "code: " + self.code + "\n"
        str += "creation: " + self.creation + "\n"
        return str

def createhash(user, pswd):
    ran = str(uuid.uuid4().hex)
    salt = hashlib.sha256( str( ran + "super secret PassTHingy herr" + user ).encode('utf-8') ).hexdigest()
    return repeated_hashing(salt, pswd)


"""
Takes a salt, and password and repeatedly hashes them 10,000 times
then returns the salt and hash combined
"""
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
        return false

