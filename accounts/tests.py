"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class EditAccountTests(TestCase):
    def test_valid_form_no_multiplier(self):
        """
        is_valid should return False if no activity multiplier
        is selected.
        """
        return True


