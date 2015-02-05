# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from board.models import Board
from android.models import User
import json
from django.core import serializers
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
# from django.views.decorators.csrf import csrf_protect
# Create your views here.

# @csrf_protect
def  createUser(request) :
	if request.method == 'POST':
		user_id = request.POST.get('user_id')
		user_age = request.POST.get('user_age')
		user_sex = request.POST.get('user_sex')

		user = User(user_id=user_id, user_age=user_age, user_sex=user_sex)
		try :
			user.save()
			return HttpResponse("Done")
		except IntegrityError :
			return HttpResponse("user id %s already exists" % user_id)

	return HttpResponse("request metod is not POST")


def getBoard(request, board_id) :
	try :
		query = Board.objects.get(id=board_id)
		resp = {}

		aPost = {}
		aPost['title_img'] = str(query.title_img)
		aPost['title'] = query.title
		aPost['content'] = query.content
		aPost['register_date'] = str(query.register_date)
		aPost['update_date'] = str(query.update_date)
		aPost['share_cnt'] = str(query.share_cnt)
		aPost['id'] = query.id
		
		resp['aPost'] = aPost
		json_data = json.dumps(resp)
		return HttpResponse(json_data)
	except ObjectDoesNotExist:
		return HttpResponse("board id %s does not exist!" % board_id)
	except MultipleObjectsReturned:
		return HttpResponse("MultipleObjectsReturned")

def push(request) :
	if request.method == 'POST':
		user_id = request.POST.get('user_id')
		try :
			query = User.objects.get(user_id=user_id)
			query.push_cnt += 1
			query.save()
			return HttpResponse("Done")

		except User.DoesNotExist :
			return HttpResponse("user id %s does not exist!" % user_id)
		except ObjectDoesNotExist:
			return HttpResponse("user id %s does not exist!" % user_id)
		except MultipleObjectsReturned:
			return HttpResponse("MultipleObjectsReturned")

	return HttpResponse("request metod is not POST")

def share(request, board_id) :
	if request.method == 'POST':
		user_id = request.POST.get('user_id')
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
			except ObjectDoesNotExist:
				return HttpResponse("user id %s does not exist!" % user_id)
			except MultipleObjectsReturned:
				return HttpResponse("user MultipleObjectsReturned")

		except Board.DoesNotExist:	
			return HttpResponse("board id %s does not exist!" % board_id)
		except ObjectDoesNotExist:
			return HttpResponse("board id %s does not exist!" % board_id)
		except MultipleObjectsReturned:
			return HttpResponse("board MultipleObjectsReturned")


def  all(request) :
	#나중에 날짜고려해서 받아야함. 지금은 임시로...
	querySet = Board.objects.filter(register_date__year=2015)
	resp = {}
	postList = []
	for obj in querySet:
		aPost = {}
		aPost['title_img'] = str(obj.title_img)
		aPost['title'] = obj.title
		aPost['id'] = obj.id
		postList.append(aPost)
	resp['post_list'] = postList
	json_data = json.dumps(resp)
	return HttpResponse(json_data)
