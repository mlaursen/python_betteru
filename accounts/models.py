from django.db import models

from utils.util import createhash

class AccountManager_old(models.Manager):
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
        )
        return account

    def create_account_from_temp(self, tmp):
        account = self.create(username=tmp.username,
                password=tmp.password,
                email=tmp.email,
				gender=None,
				units=None,
				height=None,
				activity_multiplier=None,
        )
        tmp.delete()
        return account


class Account_old(models.Model):
    GENDER_CHOICES = (
            ('select_gender', 'Select a gender'),
            ('m', 'Male'),
            ('f', 'Female'),
    )
    UNIT_CHOICES = (
            ('select_unit', 'Select a unit'),
            ('imperial', 'Imperial'),
            ('metric', 'Metric'),
    )
    MULTIPLIER_CHOICES = (
            ('select_multiplier', 'Select Activity Multiplier'),
            ('sedentary', 'Sedentary - 1.2'),
            ('lightly', 'Lightly Active - 1.375'),
            ('moderately', 'Moderately Active - 1.55'),
            ('very', 'Very Active - 1.725'),
            ('extremely','Extremely Active - 1.9'),
    )

    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    birthday = models.DateTimeField('birthday', default=None, null=True)
    gender   = models.CharField(max_length=1, choices=GENDER_CHOICES, default='select_gender')
    units    = models.CharField(max_length=8, choices=UNIT_CHOICES, default='select_unit')
    height   = models.IntegerField(default=None, null=True)
    activity_multiplier = models.CharField(max_length=10, choices=MULTIPLIER_CHOICES, default='select_multiplier')
    email    = models.CharField(max_length=40, default=None, null=True)
    active_since = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = AccountManager_old()

    def __str__(self):
        str = "user: " + self.username + "\n"
        str += "units: " + self.units + "\n"
        str += "email: " + self.email + "\n"
        return str

    def settings_complete(self):
        return self.birthday and self.gender and self.units and self.height and self.activity_multiplier



class TempAccountManager(models.Manager):
    def create_tempaccount(self, user, pswd, email, code):
        h = createhash(user, pswd)
        tmp = self.create(username=user, password=h, email=email, code=code)
        return tmp




class TempAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    email    = models.CharField(max_length=40)
    code     = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True, blank=True)

    objects = TempAccountManager()

    def __str__(self):
        str  = "user: " + self.username + "\n"
        str += "email: " + self.email + "\n"
        str += "code: " + self.code + "\n"
        return str



class AccountSettingsManager(models.Manager):
    def create_account_settings(self, account):
        return self.create(
                account=account,
                recalculate_day_of_week=1
        )




class AccountManager(models.Manager):
    def create_account_from_temp(self, tmp):
        a = self.create(
                username=tmp.username,
                password=tmp.password,
                email=tmp.email,
                gender=None,
                units=None,
                birthday=None
        )
        AccountSettings.objects.create_account_settings(a)
        tmp.delete()
        return a



class Account(models.Model):
    UNIT_CHOICES = (
            ('select_unit', 'Select a unit'),
            ('imperial', 'Imperial'),
            ('metric', 'Metric'),
    )
    GENDER_CHOICES = (
            ('select_gender', 'Select a gender'),
            ('m', 'Male'),
            ('f', 'Female'),
    )
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    email    = models.CharField(max_length=40)
    birthday = models.DateField('birthday', default=None, null=True)
    gender   = models.CharField(max_length=1, choices=GENDER_CHOICES, default='select_gender')
    units    = models.CharField(max_length=8, choices=UNIT_CHOICES, default='select_unit')
    active_since = models.DateField(auto_now_add=True)

    objects = AccountManager()

    def settings_complete(self):
        return self.birthday and self.gender and self.units

    def __str__(self):
        str  = "user: %s\n" % self.username
        str += "email: %s\n" % self.email
        str += "since: %s\n" % self.active_since
        return str





class AccountSettings(models.Model):
    MULTIPLIER_CHOICES = (
            ('select_multiplier', 'Select Activity Multiplier'),
            ('sedentary', 'Sedentary - 1.2'),
            ('lightly', 'Lightly Active - 1.375'),
            ('moderately', 'Moderately Active - 1.55'),
            ('very', 'Very Active - 1.725'),
            ('extremely','Extremely Active - 1.9'),
    )
    account                 = models.ForeignKey(Account)
    recalculate_day_of_week = models.IntegerField()
    activity_multiplier     = models.CharField(max_length=10, choices=MULTIPLIER_CHOICES, default='select_multiplier')
    height                  = models.IntegerField(default=None, null=True)
    date_changed            = models.DateField('date changed', auto_now_add=True, blank=True)

    objects = AccountSettingsManager()

    def __str__(self):
        str  = "account: %s\n" % self.account.username
        #str += "recalc: %s\n" % str(self.recalculate_day_of_week)
        #str += "changed: %s\n" % str(self.date_changed)
        #str += "mult: %s \n" % str(self.activity_multiplier)
        #str += "height: %s \n" % str(self.height)
        return str



class AccountSettingsView(models.Model):
    account = models.ForeignKey(Account)
    latest_change = models.DateField('date changed')

    class Meta:
        managed = False
        db_table = 'ACCOUNT_SETTINGS_VIEW'




class AccountView(models.Model):
    account = models.ForeignKey(Account)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    email    = models.CharField(max_length=40)
    birthday = models.DateField('birthday')
    gender   = models.CharField(max_length=1, choices=Account.GENDER_CHOICES, default='select_gender')
    units    = models.CharField(max_length=8, choices=Account.UNIT_CHOICES, default='select_unit')
    active_since = models.DateField('active since')
    latest_change = models.DateField('date changed')

    class Meta:
        managed = False
        db_table = 'ACCOUNT_VIEW'
