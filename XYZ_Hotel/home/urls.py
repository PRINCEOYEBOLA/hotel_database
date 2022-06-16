from django.urls import path
from .views import home, contact



app_name = "home"

urlpatterns = [
    path("", home, name = "homeview"),
    path("contact", contact, name = "contactview"),
    #path("adduser", adduser, name = "adduserview"),
    #path("signin/", signin, name = "signinView")
]