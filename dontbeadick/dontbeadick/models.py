from django.db import models
from datetime import datetime


class Drawing(models.Model):
	title = models.TextField()
	image = models.ImageField(upload_to=None)
	created_on = models.DateTimeField(default=datetime.now)