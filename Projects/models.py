from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Project(models.Model):
	title = models.CharField(max_length=60)
	image = models.ImageField(upload_to='images',null=True, blank=True)
	description = models.TextField(blank=True, null=True)
	body = RichTextUploadingField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

	# this will get the absolute url when interpolating in the html e.g. when using it in the hef for a image tag
	def getAbsoluteUrl(self):
		return reverse("projectDetail", kwargs={"projectId": self.id}) #f"projects/detail/{self.id}/"

	# this will display the title of the post in the admin page
	def __str__(self):
		return self.title

	# to order porjects when listed from newest to oldest
	class Meta:
		ordering = ["-timestamp"]


class Officer(models.Model):
	image = models.ImageField(upload_to='images', null=True, blank=True)
	officerName = models.CharField(max_length=50)
	officerPostion = models.CharField( max_length=65)
	isActivte = models.BooleanField(default=False)

	def __str__(self):
		return self.officerName

class Card1(models.Model):
	header = models.CharField(max_length=40)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.header
	class Meta:
		ordering = ["-pk"]
	

class Card2(models.Model):
	header = models.CharField(max_length=40)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.header

	class Meta:
		ordering = ["-pk"]

class Card3(models.Model):
	header = models.CharField(max_length=40)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.header

	class Meta:
		ordering = ["-pk"]