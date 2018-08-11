from django.db import models

# Create your models here.

class Tag(models.Model):
	name=models.CharField(max_length=55,unique=True)
	slug=models.SlugField(max_length=55,unique=True,help_text="A label to be used in urls")

class Startup(models.Model):
	name=models.CharField(max_length=55,db_index=True)
	slug=models.SlugField(max_length=55,unique=True,help_text="A label to be used in urls")
	description=models.TextField()
	founded=models.DateField('date founded')
	contact=models.EmailField()
	website=models.URLField(max_length=255)
	tags=models.ManyToManyField(Tag)

class NewsLink(models.Model):
	title=models.CharField(max_length=55)
	pub_date=models.DateField()
	link=models.URLField(max_length=255)
	startup=models.ForeignKey(Startup,on_delete=models.DO_NOTHING) # one to many relation from NewsLink to Startup means one link only can contain one startup





