# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from samplecel.tasks import hello_world

def test(request):
    hello_world.delay()
    return HttpResponse("CELERY EXAMPLE WORKING !!!!!!!!!!!!!")
