# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from board.models import Board
from android.models import User
import json
from django.core import serializers
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datetime import datetime, date, time
from django.shortcuts import render, render_to_response
# Create your views here.

# /android/user/
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

# /android/content/<board_id>/
def getBoard(request, board_id) :
	try :
		query = Board.objects.get(id = board_id)
		context = {"content" : query}
		return render(request, "android/detail.html", context)
		# return HttpResponse(json_data)
	except ObjectDoesNotExist:
		return HttpResponse("board id %s does not exist!" % board_id)
	except MultipleObjectsReturned:
		return HttpResponse("MultipleObjectsReturned")

# /android/push/
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

#  /android/share/<board_id>/
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

# /android/content/all/
def  all(request) :
	now = datetime.now()
	querySet = Board.objects.filter(update_date_start__lt=now, update_date_end__gt=now)
	resp = {}
	postList = []
	for obj in querySet:
		aPost = {}
		aPost['title_img'] = str(obj.title_img)
		aPost['title'] = obj.title
		aPost['id'] = obj.id
		aPost['register_date'] = str(obj.register_date)
		aPost['update_date_start'] = str(obj.update_date_start)
		aPost['update_date_end'] = str(obj.update_date_end)
		aPost['share_cnt'] = str(obj.share_cnt)
		postList.append(aPost)
	resp['post_list'] = postList
	json_data = json.dumps(resp)
	return HttpResponse(json_data)
