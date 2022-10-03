from django.urls import path, include
from .ajaxviews import check_username_for_uniqueness
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupView.as_view(), name="signup"),

    path('checkusername/', check_username_for_uniqueness, name='checkusername'),
]
