# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from board import forms
# Create your views here.

def  getList(request) :
	context = {}
	return render(request, "board/list.html", context)
	# return HttpResponse("안녕")

def write(request) :
	return render(request, "board/write.html", )
	# return render_to_response('write.html')

def save(request) :
	if request.method == 'POST' :
		form = forms.boardForm(request.POST)
		if form.is_valid() :
			return HttpResponseRedirect(request, "board/list.html", )
	else :
		form = boardForm()
	return HttpResponse("안녕")

# def detail(request, question_id) :
# 	return HttpResponse("You're looking at question %s." % question_id)

# def result(request, question_id) :
# 	response = "You're looking at the results of question %s."
# 	return  HttpResponse(response % question_id)

# def vote(request, question_id) :
# 	return HttpResponse("You're votiong on question %s." % question_id)
