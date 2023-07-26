from django.shortcuts import loader
from django.http import HttpResponse

def signup(request):
    template = loader.get_template("signup/signup.html")
    return HttpResponse(template.render())


# Create your views here.
