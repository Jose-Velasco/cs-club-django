from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project
from django.conf import settings
from django.core.paginator import Paginator

def home(request):
	return render(request, 'projectsHTML/index.html')
	#						^^^^ this will be rendered when it is requested by the url

def meettheofficers(request):
	return render(request, 'projectsHTML/meettheofficers.html')

def projectDetail(request, projectId):
	# this will get a specific project based on it id which will be used to be render details in projectdetail.html
	instance = get_object_or_404(Project, id=projectId)
	# context are like variables that can be rendered in the html using double curly braces with its key inbetween
	context = {
		"instance": instance,
	}
	return render(request, "projectsHTML/projectDetail.html", context)

def projects(request):
	# this will get all obbjects in the project which can be for looped in the corresponding html
	queryset_list = Project.objects.all()
	paginator = Paginator(queryset_list, 9)
	#									^^^ this is the number that will determine amount of projects per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	queryset = paginator.get_page(page)
	context = {
		"Project_list": queryset,
		"MEDIA_URL": settings.MEDIA_URL,
		"page_request_var": page_request_var,

	}
	return render(request, 'projectsHTML/projects.html', context)

def contact(request):
	return render(request, 'projectsHTML/index.html')
