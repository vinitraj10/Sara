from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Album(models.Model):
	user=models.ForeignKey(User,default='admin')
	logo=models.FileField()
	title=models.CharField(max_length=50,default=" ")
	artist=models.CharField(max_length=100,default=" ")
	genre=models.CharField(max_length=30,default=" ")
	details=models.TextField(max_length=200,default=" ")

	def __str__(self):
		return str(self.title)
class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	song_title=models.CharField(max_length=30)
	file=models.FileField(default='')

	def __str__(self):
		return str(self.song_title)