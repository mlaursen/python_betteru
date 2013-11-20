from django import forms
from django.forms import ModelForm, Form
from django.forms.util import ErrorList

from meals.models import MealPart, Meal

class CreateForm(ModelForm):
    def is_valid(self):
        valid = super(CreateForm, self).is_valid()
        return valid

    class Meta:
        model = MealPart
        fields = ['mealid',
                'ingredient',
                'amount',
                'unit',
                ]

        widgets = { 
        }
