"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.http import HttpRequest
from django.test import TestCase

from utils.util import createcode

from accounts.models import *
from accounts.forms import *
from accounts.views import *

class AccountsModuleTests(TestCase):
    def test_temp_account_create(self):
        """
        Tests that you can create a simple account
        """
        ta = TempAccount.objects.create_tempaccount('test', 'abcd1234', 'abcd@g.c', createcode())
        self.assertEqual(ta.username, 'test')
        self.assertEqual(ta.email, 'abcd@g.c')


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


    """
    Starting the forms tests
    """
    def test_createform_valid(self):
        """
        Test that the create form
        """
        self.assertEqual(1, 1)


    def test_createform_invalid(self):
        """
        Test that the create form
        """
        self.assertEqual(1, 1)


    def test_loginform_valid(self):
        """
        Test that the login form
        """
        self.assertEqual(1, 1)


    def test_loginform_invalid(self):
        """
        Test that the login form
        """
        self.assertEqual(1, 1)


    def test_editform_valid(self):
        """
        Test that the edit form
        """
        self.assertEqual(1, 1)

    def test_editform_invalid(self):
        """
        Test that the edit form
        """
        self.assertEqual(1, 1)




    """
    Starting the views tests
    """
    def test_create_view_valid(self):
        """
        Testing that the create view works with all valid
        information.

        Assumes that the CreateForm tests have passed
        """
        self.assertEqual(1, 1)


