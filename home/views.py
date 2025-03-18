from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from django.views import View
from home.models.person import Person

# Create your views here.

class HomeView(View):

    def get(self, request):
        return HttpResponse("hello World")



def list_people_view(request: HttpRequest) -> HttpResponse:

    people_response = """

        <h1>People</h1>
            <ul>

    """
    people = Person.objects.all()
    #people = people.filter(last_name='Simpson')
    # last_name='Simpson', first_name='Homer' - the comma here is treated like an AND
    people = people.exclude(last_name='Simpson', first_name='Homer').order_by("-sin")


    for person in people:
        #if person.last_name == "Simpson":
        people_response = people_response + f"<li>{person}</li>"

    people_response += "</ul>"
    return HttpResponse(people_response)
    


# def home(request):
#     return HttpResponse("hello World")