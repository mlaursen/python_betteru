"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.http import HttpRequest

from ingredients.models import *
from ingredients.forms import *
from meals.models import *

class IngredientsTests(TestCase):
    def test_create_brand(self):
        """
        Test that you can create a brand.
        """
        b = Brand.objects.create_brand('Bob')
        self.assertEqual(b.name, 'Bob')

    def test_create_brand_weird_characters(self):
        """
        Test that you can create a brand with weird characters
        """
        b = Brand.objects.create_brand("Hello Asc11_'b'")
        self.assertEqual(b.name, "Hello Asc11_'b'")


    """
    Starting category tests
    """
    def test_create_category(self):
        """
        Test that you can create a category.
        """
        c = Category.objects.create_category('Bob')
        self.assertEqual(c.name, 'Bob')

    def test_create_category_weird_characters(self):
        """
        Test that you can create a category with weird characters
        """
        c = Category.objects.create_category("Hello Asc11_'b'")
        self.assertEqual(c.name, "Hello Asc11_'b'")


    """
    Starting Ingredient tests
    """
    def test_create_ingredient_valid_all(self):
        """
        Test that you can create an ingredient with an existing brand and category
        Assumes that all Category and Brand tests have passed.
        """
        b = Brand.objects.create_brand('Test Brand')
        c = Category.objects.create_category('Test Category')
        n = 'Test Ingredient'
        def_size = 4
        def_unit = 'oz'
        alt_size = 112
        alt_unit = 'g'
        cal = 250
        fat = 17
        carb = 0
        prot = 22
        i = Ingredient.objects.create_ingredient(n, b, c, def_size, def_unit, alt_size, alt_unit, cal, fat, carb, prot)
        self.assertEqual(i.name, n)
        self.assertEqual(i.brand, b)
        self.assertEqual(i.category, c)
        self.assertEqual(i.default_serving_size, def_size)
        self.assertEqual(i.default_serving_unit, def_unit)
        self.assertEqual(i.alt_serving_size, alt_size)
        self.assertEqual(i.alt_serving_unit, alt_unit)
        self.assertEqual(i.calories, cal)
        self.assertEqual(i.fat, fat)
        self.assertEqual(i.carbohydrates, carb)
        self.assertEqual(i.protein, prot)


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
        self.test_create_ingredient_valid_all()
        i = Ingredient.objects.all()[0]
        mp = MealPart.objects.create_mealpart(mid, i.id, 4, 0)
        self.assertEqual(mp.mealid, mid)

    def test_create_mealpart_no_meal_or_ingredient(self):
        """
        Test that you can't create a meal part even if a meal doesn't exist.
        Doesn't make sense to. 
        """
        self.test_create_mealpart()
        m = Meal.objects.all()[0]
        i = Ingredient.objects.all()[0]
        mp = MealPart.objects.create_mealpart(-1, i.id, 4, 0)
        self.assertFalse(mp)
        self.assertFalse( MealPart.objects.create_mealpart(m.id, -1, 4, 0) )

    """
    Starting the forms tests
    """



    """
    Starting the views tests
    """


