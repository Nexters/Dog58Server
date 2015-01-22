# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def  getContents(request) :
	boardList = Board.objects.all()
	context = {"boardList" : boardList}
	return render(request, "board/list.html", context)