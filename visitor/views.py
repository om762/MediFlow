from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "visitor/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/workspace")
        else:
            return render(request, "Patient_app/login.html", {
                "message": "Invalid username and/or password."
            })

    return render(request, "visitor/login.html")