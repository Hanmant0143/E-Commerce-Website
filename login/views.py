from django.shortcuts import loader
from django.http import HttpResponse
def login(request):
    template=loader.get_template("login/login.html")
    return HttpResponse(template.render())

# Create your views here.
