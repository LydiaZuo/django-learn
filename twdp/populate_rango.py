import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twdp.settings')

import django
django.setup()

import random

from rango.models import Category, Page

def populate():
	python_cat = add_cat('Python')
	
	add_page(cat = python_cat,
		title = "Official Python Tutorial",
		url = "http://docs.python.org/2/tutorial/")

	add_page(cat = python_cat,
		title = "How to Think like a Computer Scientist",
		url = "http://www.greenteapress.com/thinkpython/")

	add_page(cat = python_cat,
		title = "Learn Python in 10 Minutes",
		url = "http://www.korokithakis.net/tutorials/python/")

	django_cat = add_cat("Django")

	add_page(cat = django_cat,
		title = "Official Django Tutorial",
		url = "https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

	add_page(cat = django_cat,
		title = "Django Rocks",
		url = "https://www.djangorocks.com/")

	add_page(cat = django_cat,
		title = "How to Tango with Django",
		url = "http://www.tangowithdjango.com/")

	frame_cat = add_cat("Other Frameworks")

	add_page(cat = frame_cat,
		title = "Bottle",
		url = "http://bottlepy.org/docs/dev/")

	add_page(cat = frame_cat,
		title = "Flask",
		url = "http://flask.pocoo.org")

	for c in Category.objects.all():
		for p in Page.objects.filter(category = c):
			print("- {0} - {1}".format(str(c), str(p)))
	

def add_page(cat, title, url, views = 0):
	p = Page.objects.get_or_create(category = cat, title = title, url = url)[0]
	p.save()
	return p

def add_cat(name):
	c, d = Category.objects.get_or_create(name = name)
	return c

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
#	c = Category.objects.get_or_create(name = 'Python')
#	print(c)
#	for c in Category.objects.all():
#		print(c)
	for p in Page.objects.all():
		p.views = p.views + random.randint(1, 10)
		p.save()
	
	for c in Category.objects.all():
		c.views = c.views + random.randint(1, 50)
		c.likes = c.likes + random.randint(1, 25)
		c.save()

