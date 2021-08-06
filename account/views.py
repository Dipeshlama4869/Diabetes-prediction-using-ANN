from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm

def register_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('login1')
		else:
			context['registration_form'] = form

	else: #GET_request
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register1.html', context)
	

def logout_view(request):
	logout(request)
	return redirect('prototype')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect('prototype')

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request,user)
				return redirect('prototype')

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, 'account/login1.html', context)


def video_view(request):
	return render(request, 'account/video.html',{})

def prototype(request):
	return render(request, 'account/homepage.html',{})

def description(request):
	return render(request, 'account/description.html',{})