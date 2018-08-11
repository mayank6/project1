from django.db import models
from organizer.models import Startup, Tag
# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=55)
	slug=models.SlugField(max_length=55,unique=True,help_text="A label to be used in urls",unique_for_month='pub_date') #unique for month tell to check uniqueness in a month
	description=models.TextField()
	pub_date=models.DateField('date published',auto_now_add=True)
	tags = models.ManyToManyField(Tag,related_name='blog_posts')
	startups = models.ManyToManyField(Startup,related_name='blog_posts')
	class Meta:
		verbose_name = 'blog post'
		ordering = ['-pub_date', 'title']
		get_latest_by = 'pub_date'