from django.contrib import admin
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User

# Register your models here.

class PageInline(admin.TabularInline):
	model = Page
	extra = 2

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ['name', 'slug']}),
		('Detail information', {'fields' : ['views', 'likes']}),
		]
	inlines = [PageInline]
	list_display = ['name', 'slug', 'views', 'likes']
	list_filter = ['name']

class PageAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ['category', 'title']}),
		('Detail information', {'fields' : ['url', 'views', ]}),
		]

admin.site.register(Category, CategoryAdmin)
#admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
