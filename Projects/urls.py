from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='site-home'),
    path('meettheofficers/', views.meettheofficers, name='meettheofficers'),
    path("projects/detail/<int:projectId>/", views.projectDetail, name="projectDetail"),
    #							^^^ this is used for dynamic url which is the id of the project being requested
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    
]