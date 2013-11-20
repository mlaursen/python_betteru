from django import forms
from django.forms import ModelForm, Form
from django.forms.formsets import BaseFormSet
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

class BaseMealPartForm(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        hiddenids = []
        ingredients = []
        for form in self.forms:
            hiddenid = form.cleaned_data['hiddenid']
            if hiddenid in hiddenids:
                raise forms.ValidationError("Meal Parts in a set must have different ids")
            hiddenids.append(hiddenid)
            ingredient = form.cleaned_data['ingredient']
            if ingredient in ingredients:
                raise forms.ValidationError("Two of the same ingredient. SHould combine")
            ingredients.append(ingredient)
