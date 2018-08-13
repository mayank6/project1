from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post
# Create your views here.

def blog_list(request):
	blog_list=Post.objects.all()
	context={'blogs':blog_list}
	return render(request,'organizer/blog_list.html',context)

def blog_detail(request,year,month,slug):
	blog=get_object_or_404(Post,pub_date__year=year, pub_date__month=month,slug=slug)
	context={'blog':blog}
	return render(request,'organizer/blog_detail.html',context)