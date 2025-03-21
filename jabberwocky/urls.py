
"""
URL configuration for jabberwocky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home.views import HomeView, list_people_view, people_detail_view

from django.http import HttpResponse
from django.contrib import admin
from django.urls import path


def inventory(request, *args, **kwargs):
    return HttpResponse(f"foo:{kwargs.get('foo')} and bar: {kwargs['bar']}")




urlpatterns = [
    path('<int:foo>/<str:bar>', inventory),
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('list_people/', list_people_view),
    path('people_detail_view/<int:id>/', people_detail_view)
    

]

#print(urlpatterns)
