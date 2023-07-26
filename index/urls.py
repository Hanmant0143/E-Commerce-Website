from django.urls import path
from .views import Home
app_name = 'index'
urlpatterns = [
    path('', Home, name="Home"),

]
