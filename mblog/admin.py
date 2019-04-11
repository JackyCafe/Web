from django.contrib import admin
from mblog.models import Post,PostDetail


class PostDisplay(admin.ModelAdmin):
	search_fields  = ('date1','title')
	ordering = ['-date1',]
	list_display =  ('title','date1','title')	

class PostDetailDisplay(admin.ModelAdmin):
	search_fields  = ('title',)
	list_display =  ('post_id','title','content','action','document')	
	ordering = ['post_id','-post_id',]
admin.site.register(Post,PostDisplay)	
admin.site.register(PostDetail,PostDetailDisplay)	
