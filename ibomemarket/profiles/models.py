from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

class profile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default='description default value')
	location = models.TextField(default='my location')
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
