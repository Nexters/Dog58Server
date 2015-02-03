from django.db import models

# Create your models here.
class User(models.Model) :
	user_id =  models.CharField(max_length=128, primary_key=True)
	user_age = models.IntegerField()
	user_sex = models.CharField(max_length=2)
	first_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	last_date = models.DateTimeField(auto_now=True, auto_now_add=True)
	push_cnt = models.IntegerField(default=0)
	board = models.ManyToManyField('board.Board', null=True, blank=True)

	def __unicode__(self):
		return self.user_id

	# def dic(self):
 #        		fields = ['user_id', 'user_age', 'first_date', 'last_date', 'push_cnt', 'board']
 #        		result = {}
	#         	for field in fields :
	#             		result[field] = self.__dict__[field]

	#             	return result