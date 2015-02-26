from django.db import models
from ckeditor.fields import RichTextField
	 
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os

# Create your models here.
class Board(models.Model) :
	title = models.CharField(max_length=200)
	title_img = models.ImageField(upload_to='./uploads/title/')
    	thumbnail = models.ImageField(upload_to="./uploads/thumbnails/", editable=False,blank=True,null=True)
	content = RichTextField()
	register_date = models.DateTimeField(auto_now_add = True, auto_now = True)
	update_date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
	update_date_end = models.DateTimeField(auto_now=False, auto_now_add=False)
	share_cnt = models.IntegerField(default=0)

	def create_thumbnail(self):
		if not self.title_img:
	             	return

		THUMBNAIL_SIZE = (480,360)
		try :
			DJANGO_TYPE = self.title_img.file.content_type
		except AttributeError :
			return

		if DJANGO_TYPE == 'image/jpeg':
	             	PIL_TYPE = 'jpeg'
			FILE_EXTENSION = 'jpg'
		elif DJANGO_TYPE == 'image/png':
			             PIL_TYPE = 'png'
			             FILE_EXTENSION = 'png'
			 
		image = Image.open(StringIO(self.title_img.read()))
	 
	         	# Convert to RGB if necessary
	         	# Thanks to Limodou on DjangoSnippets.org
	         	# http://www.djangosnippets.org/snippets/20/
	         	#
	         	# I commented this part since it messes up my png files
	         	#
	         	#if image.mode not in ('L', 'RGB'):
	         	#    image = image.convert('RGB')

		image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

		temp_handle = StringIO()
		image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		suf = SimpleUploadedFile(os.path.split(self.title_img.name)[-1],temp_handle.read(),content_type=DJANGO_TYPE)
		self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

	def save(self):
		self.create_thumbnail()
		super(Board, self).save()


	
	def __unicode__(self):    
        		return self.title