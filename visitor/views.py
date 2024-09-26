from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import *

def visitor_user(user):
    return user.role == 'VS'

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.role != 'VS':
            return HttpResponseRedirect(reverse('staff:workspace_view'))
        else:
            return HttpResponseRedirect(reverse('visitor:user_view'))
    return render(request, "visitor/index.html")

def login_view(request):
    if request.user.is_authenticated:
        if request.user.role != "VS":
            return HttpResponseRedirect(reverse("staff:workspace"))
        else:
            return HttpResponseRedirect(reverse('visitor:user_view'))
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.role != "VS":
                return HttpResponseRedirect(reverse("staff:workspace"))
            else:
                return HttpResponseRedirect(reverse('visitor:user_view'))
        else:
            return render(request, "visitor/login.html", {
                "message": "Invalid username and/or password."
            })

    return render(request, "visitor/login.html")

@login_required(login_url="/login")
@user_passes_test(visitor_user)
def user_view(request):
    visitor_profile = Visitor_profile.objects.get(id=request.user.profile_id)
    return render(request, "visitor/user.html" , {
        'user':request.user,
        'user_profile': visitor_profile
    })