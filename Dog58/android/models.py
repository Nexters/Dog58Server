from django.db import models

# Create your models here.
class User(models.Model) :
	user_id =  models.CharField(max_length=128)
	user_age = models.IntegerField()
	first_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	last_date = models.DateTimeField(auto_now=True, auto_now_add=True)
	push_cnt = models.IntegerField(default=0)
	board = models.ManyToManyField('board.Board')

	def __unicode__(self):    
        		return self.user_id