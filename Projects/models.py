from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

class Project(models.Model):
	title = models.CharField(max_length=60)
	image = models.ImageField(upload_to='images',null=True, blank=True)
	description = models.TextField(blank=True, null=True)
	body = RichTextUploadingField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp"]