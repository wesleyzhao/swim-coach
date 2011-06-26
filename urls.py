from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView,ListView
from meets.models import Meet,Event,Person

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swimcoach.views.home', name='home'),
    # url(r'^swimcoach/', include('swimcoach.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^$',
		ListView.as_view(
			queryset=Meet.objects.order_by('date')[:5],
			context_object_name='latest_meet_list',
			template_name='meets/index.html')),
	(r'^event/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Event,
			template_name='meets/event_detail.html')),
	(r'^(?P<meet_name>[-a-zA-Z0-9]+)/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Meet,
			template_name='meets/meet_detail.html')),
	(r'^person/(?P<person_name>[-a-zA-Z0-9]+)/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Person,
			template_name='meets/person_detail.html')),
                       url(r'^twilio_test','meets.views.twiliotest',name='twilio-test'),
                       url(r'^twilio/find_person','meets.views.get_phone_response'),
                       url(r'^add-person','meets.views.add_person'),
                       url(r'^submit-person','meets.views.submit_person'),
                       url(r'^add-number','meets.views.add_number'),
                       url(r'^submit-number','meets.views.submit_number'),
                       
)
