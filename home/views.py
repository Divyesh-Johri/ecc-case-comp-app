from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html', {})

def competition(request):
    return render(request, 'home/competition.html', {})

def team(request):
    return render(request, 'home/team.html', {})