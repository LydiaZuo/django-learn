from django.contrib import admin
from rango.models import Category, Page


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ['name', ]}),
		('Detail information', {'fields' : ['views', 'likes']}),
		]

class PageAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ['category', 'title']}),
		('Detail information', {'fields' : ['url', 'views', ]}),
		]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
