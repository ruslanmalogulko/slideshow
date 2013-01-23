from django.db import models
# To view User model:
from django.contrib.auth.models import User

# Create your models here.
class Twitters(models.Model):
	screen_name=models.CharField(max_length=100)
	text = models.CharField(max_length=160)
	img = models.CharField(max_length=400)
	aprove = models.IntegerField(max_length=1, blank=True, null=True)
	new = models.IntegerField(max_length=1, blank=True, null=True)

	def __unicode__(self):
		return self.img


class Garbage(models.Model):
	uid = models.ForeignKey(User)
	twid = models.ForeignKey(Twitters)

class Lists(models.Model):
	user = models.CharField(max_length=100)
	list_id = models.CharField(max_length=60)
	url = models.CharField(max_length=400)