from django import forms
from django.forms import ModelForm, Form
from django.forms.util import ErrorList

from meals.models import MealPart, Meal

class AddMealPartForm(ModelForm):
    hiddenid = forms.IntegerField(widget=forms.HiddenInput())

    def is_valid(self):
        valid = super(AddMealPartForm, self).is_valid()
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
class AddMealForm(ModelForm):
    
    class Meta:
        model = Meal
        fields = ['name', 'description']
        widgets = {}

