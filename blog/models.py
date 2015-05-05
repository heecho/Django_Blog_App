from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
	blog_title = models.CharField(max_length = 200)
	blog_content = models.TextField()
	user_id = models.ForeignKey(User)
	def __str__(self):
		return self.blog_content

class Comment(models.Model):
	comment_content = models.TextField()
	blog_id = models.ForeignKey(Blog)
	user_id = models.ForeignKey(User)
	def __str__(self):
		return self.comment_content
