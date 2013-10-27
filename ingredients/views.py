from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from ingredients.models import Ingredient, Category, Brand

class IndexView(generic.base.TemplateView):
    template_name = 'ingredients/index.html'

class AddView(generic.base.TemplateView):
    template_name = 'ingredients/add.html'

def index(request):
    if request.method == "POST" and request.is_ajax():
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
    else:
        ingredients = Ingredient.objects.all()
    brands = Brand.objects.all().order_by('name')
    categories = Category.objects.all()
    return render(request,
            'ingredients/index.html',
            {'ingredients': ingredients,
                'brands': brands,
                'categories': categories}
    )

