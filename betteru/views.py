# Create your views here.
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from utils.util import logged_in

def info(request):
    return render(request, 'info.html',)





