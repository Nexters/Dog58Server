# -*- coding: utf-8 -*-

from django.contrib import admin
from board.models import Board
from ckeditor.widgets import CKEditorWidget
from board.forms import BoardAdminForm

class BoardAdmin(admin.ModelAdmin) :
	list_display = ('id', 'title', 'title_img', 'content', 'register_date', 'update_date_start', 'update_date_end', 'share_cnt')
    	form = BoardAdminForm

# Register your models here.
admin.site.register(Board, BoardAdmin)