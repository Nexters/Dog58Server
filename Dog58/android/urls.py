from django.conf.urls import patterns, url, include
from android import views

urlpatterns = patterns(' ',
	url(r'^user/(?P<user_id>.+)/(?P<user_age>\d+)/(?P<user_sex>.)/$', views.createUser, name='createUser'),
	url(r'^user/(?P<user_id>\d+)/push/$', views.push, name='push'),
	url(r'^user/(?P<user_id>\d+)/(?P<board_id>\d+)/$', views.share, name='share'),
	
	url(r'^content/all/$', views.all, name='all'),
	url(r'^content/(?P<board_id>\d+)/$', views.getBoard, name='getBoard'),
)