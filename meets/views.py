# Create your views here.
from django.http import HttpResponse
from django.template import Context,loader
from meets.controller import *

def twiliotest(request):
    r = sms_response("STFU TROLOLOLOLOL")
    return HttpResponse(r)

def get_phone_response(request):
    get_attrs = request.GET
    twilio_number = get_attrs.get('From',"+14255021843")
    r = get_person_lanes(twilio_number)
    return HttpResponse(r)
