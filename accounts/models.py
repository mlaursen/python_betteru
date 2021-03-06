from django.db import models

from utils.util import createhash
from datetime import date

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
    def create_account_settings(self, account, recalc=1, height=0, activity_multiplier='sedentary'):
        return self.create(
                account=account,
                recalculate_day_of_week=recalc,
                height=height,
                activity_multiplier=activity_multiplier
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
    last_login = models.DateField('last login', auto_now_add=True)
    active_since = models.DateField(auto_now_add=True)

    objects = AccountManager()

    def settings_complete(self):
        return self.birthday and self.gender and self.units

    def update_login(self):
        self.last_login = date.today
        return self


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
    DOW_CHOICES = (
            (0, 'Select the day of week'),
            (1, 'Sunday'),
            (2, 'Monday'),
            (3, 'Tuesday'),
            (4, 'Wednesday'),
            (5, 'Thursday'),
            (6, 'Friday'),
            (7, 'Saturday'),
    )
    account                 = models.ForeignKey(Account)
    recalculate_day_of_week = models.IntegerField(choices=DOW_CHOICES, default=0)
    activity_multiplier     = models.CharField(max_length=17, choices=MULTIPLIER_CHOICES, default='select_multiplier')
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

    def update_account_settings(account, date_changed, recalculate_day_of_week=0, activity_multiplier='sedentary', height=0):
        account_settings = AccountSettings.objects.get(account=account, date_changed=date_changed)
        account_settings.recalculate_day_of_week=recalculate_day_of_week
        account_settings.activity_multiplier=activity_multiplier
        account_settings.height = height
        account_settings.save()
        return account_settings





class AccountSettingsView(models.Model):
    account = models.ForeignKey(Account)
    latest_change = models.DateField('date changed')
    recalculate_day_of_week = models.IntegerField()
    activity_multiplier     = models.CharField(max_length=17, choices=AccountSettings.MULTIPLIER_CHOICES, default='select_multiplier')
    height                  = models.IntegerField(default=None, null=True)

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
    recalculate_day_of_week = models.IntegerField(choices=AccountSettings.DOW_CHOICES, default=0)
    activity_multiplier     = models.CharField(max_length=17, choices=AccountSettings.MULTIPLIER_CHOICES, default='select_multiplier')
    height                  = models.IntegerField(default=None, null=True)
    active_since = models.DateField('active since')
    latest_change = models.DateField('date changed')

    class Meta:
        managed = False
        db_table = 'ACCOUNT_VIEW'
