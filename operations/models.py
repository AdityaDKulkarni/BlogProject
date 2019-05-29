from django.db import models

class Category(models.Model):
	word 		= models.CharField(max_length=50)
	description = models.TextField(max_length = 500, default = '')
	cover 		= models.ImageField()

	def __str__(self):
		return self.word

class Post(models.Model):

	title 			= models.CharField(max_length=100, default = '')
	description		= models.TextField(max_length = 500, default = '')
	youTubeUrl		= models.CharField(max_length=255, default = '', blank = True)
	content			= models.TextField(max_length = 500, default = '')
	category 		= models.ManyToManyField(Category, blank = True)
	tags 			= models.CharField(max_length=255, default = '', blank = True)
	summary			= models.TextField(max_length = 1000, default='', blank = True)

	def __str__(self):
		return self.title
