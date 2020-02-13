from django.db import models

# Create your models here.
class Movies(models.Model):
	title = models.CharField(max_length=100)
	year = models.IntegerField()
	score = models.FloatField()
