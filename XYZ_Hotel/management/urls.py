from django.urls import path
from .views import staff, AddUser, portal, login
from django.contrib.auth import views as auth_views


app_name = "management"

urlpatterns = [
    path("", portal, name = "portalview"),
    path("login/", auth_views.LoginView.as_view(template_name="management/login.html"), name = "loginview"),
    path("staff", staff, name = "staffview"),
    path("AddUser", AddUser, name = "adduserview"),
    path("logout/", auth_views.LogoutView.as_view(template_name="management/logout.html"), name = "logoutview"),
    #path("signin/", signin, name = "signinView")
]