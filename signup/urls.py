from django.urls import path
from .views import signup
app_name = 'signup'
urlpatterns = {

    path('',signup,name="signup"),
}