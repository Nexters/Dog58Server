# -*- coding: utf-8 -*-

from django.contrib import admin
from board.models import Board

class BoardAdmin(admin.ModelAdmin) :
	list_display = ('id', 'title')

# Register your models here.
admin.site.register(Board, BoardAdmin)