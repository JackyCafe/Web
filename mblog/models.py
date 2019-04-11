from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	id =  models.AutoField(primary_key=True)
	date1 = models.DateField(default= timezone.now) 
	title = models.CharField(max_length=200)
	finish = models.BooleanField(default = False,verbose_name='結案')
	
	class Meta:
		ordering = ('-date1',)
	
	def __str__(self):
		return self.title
	
	def decade_date(self):
		datestr =  self.date1.strftime('%Y/%m/%d')
		return datestr
		
class PostDetail(models.Model):
	id =  models.AutoField(primary_key=True)
	post_id = models.ForeignKey('Post',to_field='id',on_delete = models.CASCADE) 
	title = models.TextField(blank = True,null = True)
	content = models.TextField(blank = True,null = True)
	action = models.TextField(blank = True,null = True )
	owner = models.CharField(default='YH',max_length=10,null = True )
	due_date = models.DateField(default= timezone.now) 
	document = models.FileField(upload_to='documents/',null = True,blank = True )
	uploaded_at = models.DateTimeField(auto_now_add=True)
 