from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Memo


def index(request):
    memos = Memo.objects.all
    params = {
        'var': 'Index View Display Test',
        'memos': memos,
    }
    return render(request, 'index.html', params)
