from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import *


def index(request):
    params = {
        'var': 'Index View Display Test'
    }
    return render(request, 'index.html', params)
