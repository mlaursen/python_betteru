# Create your views here.
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from accounts.models import logged_in

def info(request):
    if logged_in(request):
        return render(request, 'info.html',)
    else:
        #msg = {'message': 'You are not logged in.  However, you can browse the website as an example user to get the feel.',
        #        'type': 'info',
        #}
        #return render(request,
        #        reverse('accounts:login'),
        #        {'msg': msg}
        #)
        return HttpResponseRedirect(reverse('accounts:login'))
