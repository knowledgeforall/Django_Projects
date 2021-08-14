#views.py

from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from myapi.models import Volunteer
from . import forms
from .forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, "index.html",)
	

def about_us(request):
    return render(request, "about_us.html",)


def contact_us(request):
    return render(request, "contact_us.html",)


def current_work(request):
    return render(request, "current_work.html",)


def donate(request):
    return render(request, "donate.html",)


def future_work(request):
    return render(request, "future_work.html",)


def Gallery(request):
    return render(request, "Gallery.html",)


def Join_Us(request):
    return render(request, "Join_Us.html",)


def members(request):
    return render(request, "members.html",)


def our_vision(request):
    return render(request, "our_vision.html",)


def our_work(request):
    return render(request, "our_work.html",)


def past_work(request):
    return render(request, "past_work.html",)


def privacy_policy(request):
    return render(request, "privacy_policy.html",)


def Resources(request):
    return render(request, "Resources.html",)


def terms_conditions(request):
    return render(request, "terms_conditions.html",)


def register_request(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'Join_Us.html', context)