"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from accounts.models import Account, TempAccount
from utils.util import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class UtilTest(TestCase):
    def test_settings_complete_empty_fields(self):
        ta = TempAccount.objects.create_tempaccount('test', 'abcd1234', 'abcd@ef.g', '432432')
        a = Account.objects.create_account_from_temp(ta)
        self.assertEqual(settings_complete(a), False)


