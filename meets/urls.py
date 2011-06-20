from django.conf.urls.defaults import *
from django.views.generic import DetailView,ListView
from meets.models import Meet

urlpatterns = patterns('',
	'''
	(r'^$',
		ListView.as_view(
			queryset=Meet.objects.order_by('date')[:5],
			context_object_name='latest_meet_list',
			template_name='meets/index.html')),

	'''
	#why does below code not work in here, but works fine in other urls.py??
	'''
	(r'^(?P<meet_name>[-a-zA-Z0-9]+)/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Meet,
			template_name='meets/detail.html')),
	'''
	
	)
'''
url(r'^(?P<pk>\d+)/results/$',
DetailView.as_view(
model=Poll,
	template_name='polls/results.html'),
		name='poll_results'),
	(r'^(?P<poll_id>\d+)/vote/$','polls.views.vote'),
'''