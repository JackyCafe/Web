from django.shortcuts import render
from .models import Entity
from _datetime import datetime

# Create your views here.
def ent_list(request):
	ent_list = Entity.obj.all()
	current_time = datetime.now	
	context = {"ent_list":ent_list}
	return render(request,'entlist.html',context)