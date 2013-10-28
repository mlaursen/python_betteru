from django.shortcuts import render, get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from ingredients.forms import CreateForm
from ingredients.models import Ingredient, Category, Brand

import sys

def index(request):
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
    if request.method == 'POST':
        f = CreateForm(request.POST)
    else:
        f = CreateForm()
    return render(request, 'ingredients/create.html', {'form': f},)

def load_table(request):
    if request.method == 'GET' and request.is_ajax():
        print("<pre>WE ARE HERE</pre>")
        category = request.GET.get('category')
        brand    = request.GET.get('brand')
        if category != 'allcategories' and category != '' and brand != 'allbrands' and brand != '':
            ingredients = Ingredient.objects.filter(category=category, brand=brand)
        elif category != 'allcategories' and category != '':
            ingredients = Ingredient.objects.filter(category=category)
        elif brand != 'allbrands' and brand != '':
            ingredients = Ingredient.objects.filter(brand=brand)
        else:
            ingredients = Ingredient.objects.all()
        brands = Brand.objects.all().order_by('name')
        categories = Category.objects.all()
        return HttpResponse('Hello')
        #return render_to_response('ingredients/index.html',
        #    {'ingredients': ingredients,
        #        'brands': brands,
        #        'categories': categories},
        #    context_instance=RequestContext(request))
    else:
        message = "This is not ajax"
        return HttpResponse(message)
