from django import forms
from django.forms import ModelForm, Form
from django.forms.util import ErrorList

from ingredients.models import Ingredient, Brand, Category
from utils.util import valid_user, createcode

class CreateForm(ModelForm):

    def is_valid(self):
        valid = super(CreateForm, self).is_valid()
        return valid

    class Meta:
        model = Ingredient
        fields = ['brand',
                'category',
                'name',
                'default_serving_size',
                'default_serving_unit',
                'alt_serving_size',
                'alt_serving_unit',
                'calories',
                'fat',
                'carbohydrates',
                'protein']
        #widgets = { 
        #    'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        #    'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        #}
