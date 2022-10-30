from django.shortcuts import render

from .models import Announcements

# Create your views here.

def home(request):
    all_announcements = Announcements.objects.all()
    return render(request, 'signin/home.html', {'announcements': all_announcements})

def signin(request):
    return render(request, 'signin/signin.html', {})

def signup(request):
    return render(request, 'signin/signup.html', {})