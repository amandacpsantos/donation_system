from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'index.html')

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')