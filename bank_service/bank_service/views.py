from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return HttpResponseRedirect("/app")
