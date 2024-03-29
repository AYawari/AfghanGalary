from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("message/", views.message, name="message"),
    path("profile/", views.account_profile, name="profile"),
]
