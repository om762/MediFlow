from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test, login_required

def staff_test(user):
    return user.role != 'VS'

# Create your views here.

@login_required(login_url="/login")
@user_passes_test(staff_test)
def workspace_view(request):
    return HttpResponse(f'hello {request.user.username}')

