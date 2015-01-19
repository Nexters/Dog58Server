from django.db import models

# Create your models here.
class Board(models.Model) :
	title = models.CharField(max_length=200)
	title_img = models.CharField(max_length=200)
	content = models.TextField()
	register_date = models.DateTimeField(auto_now_add = True, auto_now = True)
	update_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	
	def __str__(self):    
        		return self.title