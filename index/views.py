from django.shortcuts import loader
from django.http import HttpResponse

def Home(request):
    template = loader.get_template("index/index.html")
    return HttpResponse(template.render())
