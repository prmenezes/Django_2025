from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

from home.models.address import Address
from home.models.person import Person

from home.forms import AddressForm




class HomeView(TemplateView):

    template_name = "hello_world.html"

    

class PeopleView(ListView):

    # queryset = Person.objects.all()
    paginate_by = 10
    model = Person

    def post(self, request, q:str, *args, **kwargs):
        return render("hello_world.html")

    #Handling GET in html form
    def get_queryset(self):
        query_set = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_set = query_set.filter(first_name=query)

        return query_set
    

    


class PersonDetailView(DetailView):
    model = Person

class AddressListView(ListView):
    paginate_by = 20
    model = Address


class AddressDetailView(DetailView):
    model = Address

class AddressCreateView(CreateView):
    model = Address
    fields = ['street', 'unit_number', 'city', 'province', 'postal_code', 'country']

class AddressUpdateView(UpdateView):
    model = Address
    fields = ['street', 'unit_number', 'city', 'province', 'postal_code', 'country']
    #template_name_suffix = "_update_form"

class AddressDeleteView(DeleteView):
    model = Address
    success_url = reverse_lazy("address_list")

# class AddressView(View):
#     template_name = "address_form.html"
#     form_class = AddressForm
#     success_url = ""

#     def form_valid(self, form: AddressForm):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         #form.instance.save()
#         return super().form_valid(form)
#         success_url = ""

    