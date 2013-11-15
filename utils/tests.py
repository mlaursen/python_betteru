"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import datetime
from django.utils.timezone import utc
from django.test import TestCase

from accounts.models import Account, TempAccount
from utils.util import *


class UtilTest(TestCase):
    def test_valid_user_non_existing(self):
        """
        Tests that a non-existant user is not valid
        """
        self.assertEqual(valid_user('bob', 'lalalala'), False)

    def test_valid_user_existing(self):
        """
        Tests that an existing user is valid
        """
        ta = TempAccount.objects.create_tempaccount('test', 'abcd1234', 'abcd@ef.g', createcode())
        a = Account.objects.create_account_from_temp(ta)
        a.save()
        self.assertEqual(valid_user('test', 'abcd1234'), True)
    
    def test_valid_user_exising_wrong_pass(self):

        """
        Tests that an existing user with an incorrect password
        is not valid
        """
        ta = TempAccount.objects.create_tempaccount('test', 'abcd1234', 'abcd@ef.g', createcode())
        a = Account.objects.create_account_from_temp(ta)
        a.save()
        self.assertEqual(valid_user('test', 'abcd1234buffalo'), False)



    def test_get_index_of_account_genders(self):
        """
        Tests that get_index_of works on the Account.GENDER_CHOICES
        """
        self.assertEqual(get_index_of(Account.MULTIPLIER_CHOICES, 'sedentary'), 1)

    def test_get_index_of_non_exist(self):
        """
        Test that if an item does not exist, it returns False
        """
        self.assertEqual(get_index_of(Account.MULTIPLIER_CHOICES, 'bob'), False)


    def test_create_birthday_time_from_str(self):
        """
        Test that a time can be created from a string
        """
        self.assertEqual(create_birthday_time('01/01/1900'), datetime.datetime(1900, 1, 1, 0, 0, tzinfo=utc))


    def test_birthday_time_as_str_from_birthday(self):
        """
        Test that a time can be displayed in a string format
        Assumes that all create_birthday_time tests have passed.
        """
        self.assertEqual(birthday_time_as_str(create_birthday_time('01/01/1900')), '01/01/1900')

    def test_in_ttuple_exists(self):
        """
        Test that it returns true if an item exists in a tuple of tuples
        """
        ttuple = ((0, 0), (1, 1))
        self.assertTrue(in_ttuple(ttuple, 0))

    def test_in_ttuple_not_exist(self):
        """
        Test that it returns false if an item is not in a tuple of tuples
        """
        ttuple = ((0, 0), (1, 1))
        self.assertFalse(in_ttuple(ttuple, 100))
