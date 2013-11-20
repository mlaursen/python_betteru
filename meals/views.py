from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from meals.models import *
from meals.forms import *

from django.forms.formsets import formset_factory

class IndexView(generic.base.TemplateView):
    template_name = 'meals/index.html'

def add(request):
    MealPartFormSet = formset_factory(AddMealPartForm, formset=BaseMealPartForm, can_delete=True, extra=2)
    formset = MealPartFormSet()
    if request.method == 'POST':
        mf = AddMealForm(request.POST)
        mp_f = AddMealPartForm(request.POST)
        if mf.is_valid() and mp_f.is_valid():
            return HttpResponseRedirect(reverse('meals:index'))
    else:
        mf = AddMealForm()
        mp_f = AddMealPartForm()
    return render(request, 'meals/add.html', {'mp_form': mp_f,
        'm_form': mf,
        'formset': formset,})


def index(request):
    meals = MealView.objects.all()
    return render(request, 'meals/index.html', {'meals': meals,})


