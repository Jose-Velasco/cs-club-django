from django.contrib import admin
from .models import Project, Officer, Card1, Card2, Card3

class ProjectAdmin(admin.ModelAdmin):
	fields = ['title', 'image', 'description', 'body']

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		return super(ProjectAdmin, self).save_model(request, obj, form, change)


admin.site.register(Project,ProjectAdmin)
admin.site.register(Officer)
admin.site.register(Card1)
admin.site.register(Card2)
admin.site.register(Card3)