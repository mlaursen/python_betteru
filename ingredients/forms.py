from django import forms
from django.forms import ModelForm, Form
from django.forms.util import ErrorList

from ingredients.models import Ingredient, Brand, Category
from utils.util import valid_user, createcode, almost_match

class CreateForm(ModelForm):
    def clean(self):
        cleaned_data = super(CreateForm, self).clean()
        b = self.data.get('brand')

        if b != '' and b is not None:
            if not almost_match(b, Brand.objects.all()):
                Brand.objects.create_brand(b)
            brand = Brand.objects.get(name__iexact=b)
            cleaned_data['brand'] = brand

        return cleaned_data

    def is_valid(self):
        valid = super(CreateForm, self).is_valid()
        size = self.cleaned_data.get('default_serving_size')
        unit = self.cleaned_data.get('default_serving_unit')

        brand = self.cleaned_data.get('brand')

        if unit == 'unknown':
            self._errors['default_serving_unit'] = ErrorList([u"This field can not be unknown"])
            valid = False

        if brand != '':
            del self._errors['brand']
            if self._errors:
                return valid
            else:
                return True
        
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
