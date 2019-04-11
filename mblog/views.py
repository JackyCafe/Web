from django.shortcuts import render
from django.http import HttpResponse
from _datetime import datetime
from mblog.models import Post,PostDetail
from django.core.files.storage import FileSystemStorage
from django.template.loader import get_template
from django.views.generic import ListView

ITEMS_PER_PAGE = 8


# Create your views here.
def postlist(request):
	post_list = Post.objects.all()
	detail_list = PostDetail.objects.all()
	current_time = datetime.now	
	return render(request,'postlist.html',{"post_list":post_list,"detail_list":detail_list})



class postList(ListView):
	model = PostDetail
	context_object_name = 'post_list'
	template_name = 'postlist2.html'
	paginate_by = ITEMS_PER_PAGE
