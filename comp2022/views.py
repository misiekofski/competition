from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
  return render(request, 'registration/login.html')


@login_required
def index(request):
    return render(request, template_name='navbar.html')