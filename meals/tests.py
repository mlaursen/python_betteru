"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from meals.models import *
from ingredients.models import *
from ingredients.tests import IngredientsTests


class MealsTest(TestCase):
    """
    Starting the Meal tests
    """
    def test_create_meal(self):
        """
        Test that you can create a meal
        """
        n = 'Test Meal'
        d = 'test test buh buh'
        m = Meal.objects.create_meal(n, d)
        self.assertEqual(m.name, n)
        self.assertEqual(m.description, d)

    def test_create_mealpart(self):
        """
        Test that you can create a meal part
        """
        n = 'Test Meal'
        d = 'Test Meal descr'
        m = Meal.objects.create_meal(n, d)
        mid = m.id
        IngredientsTests().test_create_ingredient_valid_all()
        i = Ingredient.objects.all()[0]
        mp = MealPart.objects.create_mealpart(mid, i.id, 4, 0)
        self.assertEqual(mp.mealid, mid)

    def test_create_mealpart_no_meal_or_ingredient(self):
        """
        Test that you can't create a meal part even if a meal doesn't exist.
        Doesn't make sense to. 
        """
        self().test_create_mealpart()
        m = Meal.objects.all()[0]
        i = Ingredient.objects.all()[0]
        mp = MealPart.objects.create_mealpart(-1, i.id, 4, 0)
        self.assertFalse(mp)
        self.assertFalse( MealPart.objects.create_mealpart(m.id, -1, 4, 0) )

    """
    Starting views testing here
    """

    """
    Starting forms testing here
    """


