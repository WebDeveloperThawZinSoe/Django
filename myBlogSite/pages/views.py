# import Http Response from django
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# create a function
def index(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "title" : "Testing Page"
    }
    # return response with template and context
    return render(request, "index.html", context)
