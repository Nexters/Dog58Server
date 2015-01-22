# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from board.models import Board
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
# Create your views here.

def  createUser(request) :
	return HttpResponse()
def  all(request) :
	#나중에 날짜고려해서 받아야함. 지금은 임시로...
	querySet = Board.objects.filter(register_date__year=2015)
	data = serializers.serialize('json', list(querySet), fields=('title','title_img'))
	# listJson = json.dumps(list(querySet), cls=DjangoJSONEncoder)
	return HttpResponse(data, content_type="application/json")