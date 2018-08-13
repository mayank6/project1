from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Tag,Startup
# Create your views here.
def tag_list(request):
	tag_list=Tag.objects.all()
	context={"tag_list":tag_list}
	return render(request,'organizer/tag_list.html',context)

def tag_detail(request,slug):
	tag=get_object_or_404(Tag,slug__iexact=slug)
	context={"tag":tag}
	return render(request,'organizer/tag_detail.html',context)

def startup_list(request):
	startup=Startup.objects.all()
	context={'startup':startup}
	return render(request,'organizer/startup_list.html',context)

def startup_detail(request,slug):
	startup=get_object_or_404(Startup,slug__iexact=slug)
	context={'startup':startup}
	return render(request,'organizer/startup_detail.html',context)