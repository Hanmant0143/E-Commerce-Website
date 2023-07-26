# import datetime
from django.template import loader
from django.http import HttpResponse
# from django.shortcuts import render
def courses(request):
    template = loader.get_template("courses/courses.html")
    return HttpResponse(template.render())
def testing(request):
    template = loader.get_template("courses/testing.html")
    return HttpResponse(template.render())

def introduction02(request):
    template = loader.get_template("courses/html/introduction02.html")
    return HttpResponse(template.render())
# Create your views here.
