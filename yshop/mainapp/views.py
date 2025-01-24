from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

# Create your views here.

def home(request):
    context = {} # context dictionary for passing for rendering
    template = loader.get_template('home.html') #creating a template object from the desgined template ht
    return HttpResponse(template.render(context, request)) # creating a response object after rendering
    #the returned response has the html of completed webpage including required data
