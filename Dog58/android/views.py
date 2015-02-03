# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from board.models import Board
from android.models import User
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db import IntegrityError
# Create your views here.

#미완, save되는지 안되는지 확인 필요할 듯

def  createUser(request, user_id, user_age, user_sex) :
	try :
		user = User(user_id=user_id, user_age=user_age, user_sex=user_sex)
		user.save()
		return HttpResponse("Done")
	except IntegrityError :
		return HttpResponse("user id %s already exists" % user_id)

def getBoard(request, board_id) :
	query = Board.objects.get(id=board_id)
	resp = {}

	aPost = {}
	aPost['title_img'] = str(query.title_img)
	aPost['title'] = query.title
	aPost['content'] = query.content
	aPost['register_date'] = str(query.register_date)
	aPost['update_date'] = str(query.update_date)
	aPost['share_cnt'] = str(query.share_cnt)
	
	resp['aPost'] = aPost
	json_data = json.dumps(resp)
	return HttpResponse(json_data)

def push(request, user_id) :
	try :
		query = User.objects.get(user_id=user_id)
		query.push_cnt += 1
		query.save()
		return HttpResponse("Done")

	except User.DoesNotExist :
		return HttpResponse("user id %s does not exist!" % user_id)

def share(request, user_id, board_id) :
	try :
		boardQuery = Board.objects.get(id=board_id)
		boardQuery.share_cnt += 1
		boardQuery.save()
		try :
			userQuery = User.objects.get(user_id=user_id)
			userQuery.board.add(boardQuery)
			return HttpResponse("Done")

		except User.DoesNotExist:	
			return HttpResponse("user id %s does not exist!" % user_id)

	except Board.DoesNotExist:	
		return HttpResponse("board id %s does not exist!" % board_id)

def  all(request) :
	#나중에 날짜고려해서 받아야함. 지금은 임시로...
	querySet = Board.objects.filter(register_date__year=2015)
	resp = {}
	postList = []
	for obj in querySet:
		aPost = {}
		aPost['title_img'] = str(obj.title_img)
		aPost['title'] = obj.title
		postList.append(aPost)
	resp['post_list'] = postList
	json_data = json.dumps(resp)
	return HttpResponse(json_data)
