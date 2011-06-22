# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context,loader,RequestContext
from meets.controller import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

def twiliotest(request):
    r = sms_response("STFU TROLOLOLOLOL")
    return HttpResponse(r)

def get_phone_response(request):
    get_attrs = request.GET
    twilio_number = get_attrs.get('From',"+14255021843")
    r = get_person_lanes(twilio_number)
    return HttpResponse(r)

def add_person(request):
    t = loader.get_template('meets/add-person.html')
    c = RequestContext(request, { 
            #some variable
            })
    return HttpResponse(t.render(c))

def submit_person(request):
    name = request.POST['name-value']
    name_arr = name.split(' ',1)
    error_message = ""
    if len(name_arr)<2:
        error_message = 'Please add a last name!'
    elif Person.objects.filter(first_name=name_arr[0],last_name=name_arr[1]):
        error_message = name + " is already registered!"
    else:
        p = Person(first_name=name_arr[0],last_name=name_arr[1])
        p.save()
    if error_message:
        return render_to_response('meets/add-person.html',{
               'error_message':error_message,
               }, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('meets.views.add_person'))

def add_number(request):
    ##do stuff

def save_number(request):
    ##do more stuff
