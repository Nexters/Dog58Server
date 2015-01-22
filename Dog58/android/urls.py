from django.conf.urls import patterns, url, include
from android import views

urlpatterns = patterns(' ',
	url(r'^user/(?P<user_id>\d+)/(?P<user_age>\d+)/$', views.createUser, name='createUser'),
	url(r'^content/all/$', views.all, name='all'),
)