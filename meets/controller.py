import twilio
from meets.models import Meet,Event,Person,Lane,PhoneNumber
def sms_response(response_text):
    r = twilio.Response()
    r.append(twilio.Sms(response_text))
    return r

def get_person_with_number(phone_number):
    '''returns empty string if person does not exist, otherwise returns the person object that belongs to the phone_number'''
    try:
        phone = PhoneNumber.objects.get(number=phone_number)
        try:
            person = phone.person
        except:
            person = ''
        return person
    except:
        return ''

def strip_twilio_number(twilio_phone):
    '''takes string representation of twilio phone number and returns an integer phone_number'''
    num = int(twilio_phone[2:])
    return num

def make_twilio_number(phone_number):
    '''phone_number is an integer, and returns a string format twilio number'''
    return "+1"+str(phone_number)

def get_person_lanes(twilio_number):
    phone_number = strip_twilio_number(twilio_number)
    person = get_person_with_number(phone_number)
    r = twilio.Response()
    if person:
        lanes = person.lane_set.all()
        if lanes:
            events_text = ""
            #for lane in lanes:
            #   events_text = lane.event.name + " (Event #" + str(lane.event.number) + ") Lane #" + str(lane.number)
            event_list = [(lane.event.name + " (Event #" + str(lane.event.number) + ") Lane #" + str(lane.number)) for lane in lanes]
            events_text = ", ".join(event_list)+"."
        else:
            events_text = "nothing."
        text = person.first_name + " " + person.last_name + " is competing in " + events_text
    else:
        #end if person:
        text = "No name seems to be associated with this number"
    r.append(twilio.Sms(text))
    return r
