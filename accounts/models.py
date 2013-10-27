from django.db import models

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
