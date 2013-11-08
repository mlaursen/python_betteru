from django import forms
from django.forms import ModelForm, Form
from django.forms.util import ErrorList

from ingredients.models import Ingredient, Brand, Category
from utils.util import valid_user, createcode

class CreateForm(ModelForm):

    def is_valid(self):
        valid = super(CreateForm, self).is_valid()
        size = self.cleaned_data.get('default_serving_size')
        unit = self.cleaned_data.get('default_serving_unit')

        alt_size = self.cleaned_data.get('alt_serving_size')
        alt_unit = self.cleaned_data.get('alt_serving_unit')

        if unit == 'unknown':
            self._errors['default_serving_unit'] = ErrorList([u"This field can not be unknown"])
            valid = False

        
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

        widgets = { 
            'name': forms.TextInput(attrs={'placeholder': 'Ingredient Name'}),
            'default_serving_size': forms.TextInput(attrs={'placeholder': 'Default serving size'}),
            'alt_serving_size': forms.TextInput(attrs={'placeholder': 'Alternate serving size'}),
            'calories': forms.TextInput(attrs={'placeholder': '(kCal)'}),
            'fat': forms.TextInput(attrs={'placeholder': '(g)'}),
            'carbohydrates': forms.TextInput(attrs={'placeholder': '(g)'}),
            'protein': forms.TextInput(attrs={'placeholder': '(g)'}),
        }
