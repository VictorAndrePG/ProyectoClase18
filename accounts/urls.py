from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import login_request, register_request

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('register/', register_request, name="Register"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
]


