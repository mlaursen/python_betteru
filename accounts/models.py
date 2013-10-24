from django.db import models

# Create your models here.
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


    def __str__(self):
        str = "user: " + self.username + "\n"
        str += "birthday: " + self.birthday + "\n"
        str += "units: " + self.units + "\n"
        str += "height: " + self.height + "\n"
        str += "acti-mult: " + self.activity_multiplier + "\n"
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
