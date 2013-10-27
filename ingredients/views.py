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
    ingredients = Ingredient.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    return render(request,
            'ingredeints/index.html',
            {'ingredients': ingredients,
                'brands': brands,
                'categories': categories}
    )

