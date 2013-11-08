"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from accounts.models import *
from utils.util import createcode


class TempAccountTest(TestCase):
    def test_temp_account_create(self):
        """
        Tests that you can create a simple account
        """
        ta = TempAccount.objects.create_tempaccount('test', 'abcd1234', 'abcd@g.c', createcode())
        self.assertEqual(ta.username, 'test')
        self.assertEqual(ta.email, 'abcd@g.c')


class AccountTest(TestCase):
    def test_create_account_from_temp(self):
        """
        Tests that you can create an account from a temp account.
        Assumes that the TempAccountTest class has no failures

        Fails because you can't insert NULL into id..
        """
        ta = TempAccount.objects.create_tempaccount('test', 'abcd1234', 'abcd@g.c', createcode())
        a = Account.objects.create_account_from_temp(ta)
        self.assertEqual(a.username, ta.username)
        self.assertEqual(a.password, ta.password)
        self.assertEqual(a.email, ta.email)
        self.assertEqual(a.birthday, None)
        self.assertEqual(a.activity_multiplier, None)
        self.assertEqual(a.units, None)
        self.assertEqual(a.gender, None)




