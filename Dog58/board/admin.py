# -*- coding: utf-8 -*-

from django.contrib import admin
from board.models import Board
from ckeditor.widgets import CKEditorWidget
from board.forms import BoardAdminForm

class BoardAdmin(admin.ModelAdmin) :
<<<<<<< HEAD
	list_display = ('id', 'title', 'title_img', 'content', 'register_date', 'update_date')
=======
	list_display = ('id', 'title', 'title_img', 'content', 'register_date', 'update_date', 'share_cnt')
>>>>>>> LimHeeJho
    	form = BoardAdminForm

# Register your models here.
admin.site.register(Board, BoardAdmin)