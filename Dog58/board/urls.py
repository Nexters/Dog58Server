from django.conf.urls import patterns, url
from board import views

urlpatterns = patterns(' ',
	url(r'^$', views.getList, name = 'getList'),
	url(r'^write/$', views.write, name='write'),
	url(r'^save/$', views.save, name='save'),
)