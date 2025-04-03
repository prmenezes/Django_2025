from django.shortcuts import render

from django.views.generic.base import TemplateView
from home.models.person import Person
from home.models.address import Address

# Create your views here.



class HomeView(TemplateView):

    template_name = "hello_world.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "guy"
        return context
    

class PeopleView(TemplateView):

    template_name = "people_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["people"] = Person.objects.all()
        return context
    

class PersonDetailView(TemplateView):

    template_name = "person_detail_view.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person"] = Person.objects.get(pk=id)
        return context



