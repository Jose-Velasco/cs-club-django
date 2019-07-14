from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project
from django.conf import settings

def home(request):
	return render(request, 'projectsHTML/index.html')

def meettheofficers(request):
	return render(request, 'projectsHTML/index.html')

def projectDetail(request, projectId):
	instance = get_object_or_404(Project, id=projectId)
	context = {
		"instance": instance,
	}
	return render(request, "projectsHTML/projectDetail.html", context)

def projects(request):
	queryset = Project.objects.all()
	context = {
		"Project_list": queryset,
		"MEDIA_URL": settings.MEDIA_URL
	}
	return render(request, 'projectsHTML/projects.html', context)

def contact(request):
	return render(request, 'projectsHTML/index.html')
