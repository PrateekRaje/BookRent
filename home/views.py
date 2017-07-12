# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def profile(request):
	return render(request, 'home/profile.html',)


def index(request):
    return render(request, 'home/home.html',)	