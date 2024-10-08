from django.urls import path
from . import views

app_name = "visitor"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("user", views.user_view, name="user_view")
]
