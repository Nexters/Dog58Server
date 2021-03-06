# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from board.models import Board
from board.forms import BoardAdminForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
# Create your views here.

def  getList(request) :
	boardList = Board.objects.all()
	context = {"boardList" : boardList}
	return render(request, "board/list.html", context)

def get(request, board_id) :
	board = Board.objects.get(id = board_id)
	context = {"content" : board}
	return render(request, "board/content.html", context)

def write(request):
	form = BoardAdminForm()
	tpl  = "board/write.html"
	return render(request, tpl, {"form" : form}) 

def save(request) :
	return HttpResponseRedirect(reverse('board:getList'))

def delete(request, board_id) :
	board = Board.objects.get(id = board_id)
	# try : 
	board.delete()
	# except :
	return HttpResponseRedirect(reverse('board:getList'))