from django.db import models

# Create your models here.

class Tag(models.Model):
	name=models.CharField(max_length=55,unique=True)
	slug=models.SlugField(max_length=55,unique=True,help_text="A label to be used in urls")
	class Meta:
		ordering=['name'] #to order our Tag model alphabetically by the model’s name
	def __str__(self):
		return self.name	

class Startup(models.Model):
	name=models.CharField(max_length=55,db_index=True)
	slug=models.SlugField(max_length=55,unique=True,help_text="A label to be used in urls")
	description=models.TextField()
	founded=models.DateField('date_founded')
	contact=models.EmailField()
	website=models.URLField(max_length=255)
	tags=models.ManyToManyField(Tag)
	class Meta:
		ordering=['name']
		get_latest_by='date_founded'

	def __str__(self):
		return self.name

class NewsLink(models.Model):
	title=models.CharField(max_length=55)
	pub_date=models.DateField()
	link=models.URLField(max_length=255)
	startup=models.ForeignKey(Startup,on_delete=models.DO_NOTHING) # one to many relation from NewsLink to Startup means one link only can contain one startup
	class Meta:
		verbose_name = 'news article'
		ordering = ['-pub_date']
		get_latest_by = 'pub_date'
	def __str__(self):
		return self.title




