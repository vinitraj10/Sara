from django.db import models

# Create your models here.
class Album(models.Model):
	logo=models.FileField()
	tilte=models.CharField(max_length=50,default=0)
	artist=models.CharField(max_length=100,default="Vinit")
	genre=models.CharField(max_length=30,default="Rock")
	details=models.TextField(max_length=200,default=0)

	def __str__(self):
		return str(self.tilte)