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
    	return render(request, "board/write.html", {"form" : BoardAdminForm()}) 

def save(request) :
	# if request.method == 'POST' :
	# 	form = BoardAdminForm(request.POST)
	# 	if form.is_valid() :
	# 		return HttpResponseRedirect(request, "board/list.html", )
	# else :
	# 	form = boardForm()
	return HttpResponseRedirect(reverse('board:getList'))

#롤백 구현 추가하기
def delete(request, board_id) :
	board = Board.objects.get(id = board_id)
	# try : 
	board.delete()
	# except :
	#에러 원인 뭔지 찾기
	return HttpResponseRedirect(reverse('board:getList'))