from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.conf import settings

def home(request):
	return render(request, 'projectsHTML/index.html')

def meettheofficers(request):
	return render(request, 'projectsHTML/index.html')

def projects(request):
	queryset = Project.objects.all()
	my_context = {
		"Project_list": queryset,
		"range": 5,
		"n": range(5),
		'title':'Projects',
		"MEDIA_URL": settings.MEDIA_URL
	}
	return render(request, 'projectsHTML/projects.html', my_context)

def contact(request):
	return render(request, 'projectsHTML/index.html')
