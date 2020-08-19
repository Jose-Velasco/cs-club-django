from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from .models import Project, Officer, Card1, Card2, Card3, ContactForm
from django.conf import settings
from django.core.paginator import Paginator
from django.views import View
import requests
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from .forms import ContactUsForm
from django import forms

@csrf_protect
def home(request):
	card1List = Card1.objects.first()
	card2List = Card2.objects.first()
	card3List = Card3.objects.first()
	form = ContactUsForm()

	context = {
		"card1": card1List,
		"card2": card2List,
		"card3": card3List,
		"form": form,	
	}
	if request.method == "POST":
		form = ContactUsForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			email = form.cleaned_data["email"]
			subject = form.cleaned_data["subject"]
			newContactForm = ContactForm(name=name,email=email,subject=subject)
			newContactForm.save()
		return HttpResponseRedirect(request.path_info)

	return render(request, 'projectsHTML/index.html', context)
	#						^^^^ this will be rendered when it is requested by the url

def meettheofficers(request):
	activeOfficersList = Officer.objects.filter(isActivte=True)
	notActiveOfficers = Officer.objects.filter(isActivte=False)

	context = {
		"activeOfficers": activeOfficersList,
		"notActivteOfficers": notActiveOfficers,
		"MEDIA_URL": settings.MEDIA_URL,
	}
	return render(request, 'projectsHTML/meettheofficers.html', context)

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
		# do not forget to pass the url so it can find the right path to the images(might have to be adjusted on deplyment
		# if there are any erros)
		"MEDIA_URL": settings.MEDIA_URL,
		"page_request_var": page_request_var,

	}
	return render(request, 'projectsHTML/projects.html', context)

def contact(request):
	return render(request, 'projectsHTML/index.html')

# using this to temp solve issues when trying to reset password on my 
# flashcard app(the issue comes because my flashcard app API uses http
# and not https thus firebase will not send post request to servers
# that are not sequred with https & i do not want to buy another domain)
# decorator allows me to receive post request from external site that i
# have not provided csrf tokens for
@method_decorator(csrf_exempt, name='dispatch')
class FlashcardAppPasswordRest(View):
	def post(self, request, *args, **kwargs):
		url = "http://45.79.225.82/password/reset/confirm/"
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		req = requests.post(url, json = body)
		return JsonResponse(req.json(), status=req.status_code)
