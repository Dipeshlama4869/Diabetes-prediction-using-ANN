"""FortellStocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from content.views import (
	home_view,
)

from account.views import (
	register_view,
	logout_view,
	login_view,
    video_view,
    prototype,
    description,
)


from predict.views import(
    predict_view,
    result,
)
from information.views import(
    information_view,
)

from video.views import(
    video_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', prototype, name="prototype"),
    path('register/', register_view, name="register1"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login1"),
    path('video/', video_view, name="video"),
    path('predict/', predict_view, name="predict"),
    path('predict/result', result, name="result"),
    path('information/', information_view, name="information"),
    path('video/', video_view, name="video"),
    path('description/', description, name='description')
]
