from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def new_user(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.groups = 1
            user.save()
            return redirect('login')

    return render(request, 'new_user.html', {'form': form})

def update_user(request):
    pass

def delete_user(request):
    pass

def list_user(request):
    pass

def profile_user(request):
    return render(request, 'profile_user.html')