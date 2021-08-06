from django.shortcuts import render

# Create your views here.
def information_view(request):
	return render(request, 'information/information.html', {})