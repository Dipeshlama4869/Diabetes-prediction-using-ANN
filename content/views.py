from django.shortcuts import render

#Views

#Home screen view

def home_view(request):
	print(request.headers)
	return render(request, 'base.html', {})
