from django.urls import path
from .views import courses,testing,introduction02
app_name = 'courses'
urlpatterns= {
    path('',courses,name="courses"),
    path('testing/',testing,name="testing"),
    path('html-introduction02/',introduction02,name="introduction02")
}