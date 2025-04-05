from django.shortcuts import render

from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from home.models.person import Person
from home.forms import AddressForm

# Create your views here.

# class SearchContextMixin:
        
#         def get_context_data(self, **kwargs):
#             context =  super().get_context_data(**kwargs)
#             context["search_form"] = PeopleSearchForm()
#             return context


class HomeView(TemplateView):

    template_name = "hello_world.html"

    

class PeopleView( ListView):

    # queryset = Person.objects.all()
    paginate_by = 10
    model = Person

    # def post(self, request, q:str, *args, **kwargs):
    #     return render("hello_world.html")

    #Handling GET in html form
    def get_queryset(self):
        query_set = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_set = query_set.filter(first_name=query)

        return query_set
    

    


class PersonDetailView(DetailView):

    model = Person



class AddressView(View):

    def get(self, request, *args, **kwargs):
        context  = {
            "form" : AddressForm()
        }

        return render(request, "address_form.html", context)
    

    def post(self, request, *args, **kwargs):

        address = AddressForm(data=request.POST)
        if address.is_valid():
            address.instance.save()

        context  = {
            "form" : address
        }

        return render(request, "address_form.html", context)