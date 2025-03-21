from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from django.views import View
from home.models.person import Person
from home.models.address import Address

# Create your views here.

# class AddressView(View):

#     def get(self, request):
#         return HttpResponse("address")
    
#     def list_address():

class HomeView(View):

    def get(self, request):

        context = {
            "username": "guy"
        }
        #return HttpResponse("hello World")
        return render(request, "hello_world.html", context=context)



def list_people_view(request: HttpRequest) -> HttpResponse:

    # people_response = """

    #     <h1>People</h1>
    #         <ul>

    # """
    #people = Person.objects.all()
    #people = people.filter(last_name='Simpson')
    # last_name='Simpson', first_name='Homer' - the comma here is treated like an AND
    #people = people.exclude(last_name='Simpson', first_name='Homer').order_by("-sin")
    #people = people.filter(address__province__iexact='sk')



    # for person in people:
    #     #if person.last_name == "Simpson":
    #     people_response = people_response + f"<li>{person}</li>"

    # people_response += "</ul>"
    # return HttpResponse(people_response)
    silly_things = {
        "people": Person.objects.all()
        #"people": Person.objects.filter(first_name="billy")
    }
    return render(request, "people_view.html", context=silly_things)
    
# def people_detail_view(request: HttpRequest, id:int) -> HttpResponse:
#     silly_things = {
#         "people": Person.objects.all()
#     }
#     return render(request, "people_view.html", context=silly_things)



# def home(request):
#     return HttpResponse("hello World")