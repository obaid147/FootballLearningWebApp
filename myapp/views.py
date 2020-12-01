from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contents = {
        'title': 'Home',
        'heading': 'Soccer Learning'
    }
    return render(request, 'index.html', contents)

def overview(request):
    contents = {
        'title': 'Overview',
        'heading': 'OVERVIEW'
    }
    return render(request, 'overview_1.html', contents)

def skills(request):
    contents = {
        'title': 'Skills',
        'heading': 'SKILLS'
    }
    return render(request, 'skills.html', contents)


def about(request):
    contents = {
        'title': 'About',
        'heading': 'ABOUT US'
    }
    return render(request, 'about.html', contents)