from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Board(models.Model) :
	title = models.CharField(max_length=200)
	title_img = models.ImageField(upload_to='./uploads/title/')
	content = RichTextField()
	register_date = models.DateTimeField(auto_now_add = True, auto_now = True)
	update_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	share_cnt = models.IntegerField(default=0)
	
	def __unicode__(self):    
        		return self.title_img