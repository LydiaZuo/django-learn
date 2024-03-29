from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required

from datetime import datetime
def index(request):
	context_dict = {}

	category_list = Category.objects.order_by('-likes')[:5]
	context_dict['categories'] = category_list

	page_list = Page.objects.order_by('-views')[:10]
	context_dict['pages'] = page_list

	visits = int(request.COOKIES.get('visits', '1'))
	print(visits)

	reset_last_visit_time = False
	response = render(request, 'rango/index.html', context_dict)

	if 'last_visit' in request.COOKIES:
		last_visit = request.COOKIES['last_visit']
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

		if (datetime.now() - last_visit_time).days > 0:
			visits = visits + 1
			reset_last_visit_time = True
	else:
		reset_last_visit_time = True

		context_dict['visits'] = visits
		response = render(request, 'rango/index.html', context_dict)
	
	if reset_last_visit_time:
		response.set_cookie('last_visit', datetime.now())
		response.set_cookie('visits', visits)
	return response

def about(request):
	context_dict = {'aboutmessage': "Never mind, here is the about page."}
	return render(request, 'rango/about.html', context_dict)
	
def category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug = category_name_slug)
		context_dict['category_name'] = category.name

		pages = Page.objects.filter(category = category)

		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass

	return render(request, 'rango/category.html', context_dict)

@login_required
def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print(form.errors)

	else:
		form = CategoryForm()

	return render(request, 'rango/add_category.html', {'form':form})

@login_required
def add_page(request, category_name_slug):
	try:
		cat = Category.objects.get(slug = category_name_slug);
	except Category.DoesNotExist:
		cat = None

	if request.method == 'POST':
		form = PageForm(request.POST)
		
		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.category = cat
				page.views = 0
				page.save()
				return category(request, category_name_slug)
		else:
			print(form.errors)
	
	else:
		form = PageForm()

	context_dict = {'form':form, 'category': cat}

	return render(request, 'rango/add_page.html', context_dict)

'''
def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit = False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'rango/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
'''

'''
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/rango/')
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplies.")

	else:
		return render(request, 'rango/login.html', {})
'''


@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")


'''
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/rango/')
'''





















