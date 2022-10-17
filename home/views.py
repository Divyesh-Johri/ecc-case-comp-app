from django.shortcuts import render

from .models import Announcements

def home(request):
    all_announcements = Announcements.objects.all()
    return render(request, 'home/home.html', {'announcements': all_announcements})

def competition(request):
    return render(request, 'home/competition.html', {})

def team(request):
    return render(request, 'home/team.html', {})

def signin(request):
    return render(request, 'home/signin.html', {})

def signup(request):
    return render(request, 'home/signup.html', {})