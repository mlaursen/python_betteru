from django.shortcuts import render, get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from ingredients.forms import CreateForm
from ingredients.models import Ingredient, Category, Brand

import sys, re

def index(request):
    if request.is_ajax():
        ingredients = Ingredient.objects.get(pk=2)
    else:
        ingredients = Ingredient.objects.all()
    brands = Brand.objects.all().order_by('name')
    categories = Category.objects.all()
    return render_to_response('ingredients/index.html',
            {'ingredients': ingredients,
                'brands': brands,
                'categories': categories},
            context_instance=RequestContext(request)
    )

def home(request):
    return render_to_response('ingredients/home.html',
            {},
            context_instance=RequestContext(request))

def create(request):
    b = list(Brand.objects.all())
    b.reverse()
    b.append('New Brand')
    b.reverse()
    c = Category.objects.all()
    if request.method == 'POST':
        f = CreateForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data.get('name')
            brand = f.cleaned_data.get('brand')
            catg = f.cleaned_data.get('category')
            dss = f.cleaned_data.get('default_serving_size')
            dsu = f.cleaned_data.get('default_serving_unit')
            ass = f.cleaned_data.get('alt_serving_size')
            asu = f.cleaned_data.get('alt_serving_unit')
            calories = f.cleaned_data.get('calories')
            fat = f.cleaned_data.get('fat')
            carbs = f.cleaned_data.get('carbohydrates')
            prot = f.cleaned_data.get('protein')
            i = Ingredient.objects.create_ingredient(name, brand, catg, dss, dsu, ass, asu, calories, fat, carbs, prot)
            i.save()
            return HttpResponseRedirect(reverse('ingredients:index'))
    else:
        f = CreateForm()
    return render(request, 'ingredients/create.html', {'form': f,
        'categories': c,
        'brands': b},)

def load_table(request):
    brands = Brand.objects.all().order_by('name')
    categories = Category.objects.all()
    if request.is_ajax():
        category = request.GET.get('category')
        brand    = request.GET.get('brand')
        if category and not match_all(category) and brand and not match_all(brand):
            ingredients = Ingredient.objects.filter(category=category, brand=brand)
        elif category and not match_all(category):
            ingredients = Ingredient.objects.filter(category=category)
        elif brand and not match_all(brand):
            ingredients = Ingredient.objects.filter(brand=brand)
        else:
            ingredients = Ingredient.objects.all()
        return render_to_response('ingredients/ingredient_table.html',
            {'ingredients': ingredients,
                'brands': brands,
                'categories': categories},
            context_instance=RequestContext(request))
    else:
        message = "This is not ajax"
        return HttpResponse('Goodbye')

def match_all(n):
    return re.match("[A-z]*all", n)

