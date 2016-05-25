from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def homepage(request):
    return render_to_response('intro.html', locals(),
        context_instance=RequestContext(request),)

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def wiki(request):
    return render_to_response('about.html', locals(),
        context_instance=RequestContext(request),)

def contact(request):
    return render_to_response('contact.html', locals(),
        context_instance=RequestContext(request),)
