from django.contrib import admin
from android.models import User
# Register your models here.
# -*- coding: utf-8 -*-

class UserAdmin(admin.ModelAdmin) :
	list_display = ('user_id', 'user_age', 'user_sex', 'first_date', 'last_date', 'push_cnt',)
    	filter_horizontal = ('board',)
# Register your models here.
admin.site.register(User, UserAdmin)