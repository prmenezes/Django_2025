from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from home.models.person import Person
from home.models.address import Address

# Create your views here.



class HomeView(TemplateView):

    template_name = "hello_world.html"

    

class PeopleView(ListView):

    # queryset = Person.objects.all()
    paginate_by = 10
    model = Person


class PersonDetailView(DetailView):

    model = Person



