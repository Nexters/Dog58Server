from django.conf.urls import patterns, url, include
from android import views

urlpatterns = patterns(' ',
	# url(r'^user/$', views.user, name='user'),
	# url(r'^$', views.getList, name = 'getList'),
	# url(r'^(?P<board_id>\d+)/$', views.get, name='get'),
	# url(r'^write/$', views.write, name='write'),
	# url(r'^save/$', views.save, name='save'),
	# url(r'^delete/(?P<board_id>\d+)/$', views.delete, name='delete'),
	url(r'^user/(?P<user_id>\d+)/(?P<user_age>\d+)/$', views.createUser, name='createUser'),
	url(r'^content/all/$', views.all, name='all'),
)