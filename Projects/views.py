from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'projects/home.html')

def meettheofficers(request):
	return render(request, 'projects/home.html')

def projects(request):
	return render(request, 'projects/projects.html', {'title':'Projects'})

def contact(request):
	return render(request, 'projects/home.html')
