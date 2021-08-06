from django.shortcuts import render

# Create your views here.
def video_view(request):
	return render(request, 'video/video.html',{})