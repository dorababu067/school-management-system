from django.shortcuts import render
from .models import School

# Create your views here.


def index(request):

    if request.method == "POST":
        # get the school, address values form html page, which user has submitted.
        name = request.POST.get("name")
        address = request.POST.get("address")

        school = School(name=name, address=address)
        school.save()
        return render(request, "index.html")
    if request.method == "GET":
        return render(request, "index.html")
