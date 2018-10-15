from django.contrib.auth import get_user
from django.shortcuts import render, redirect, get_object_or_404
from user.models import Person
from .forms import UserForm, UserFormUp
from django.contrib.auth.models import User


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
    user = get_object_or_404(Person, pk=get_user(request).pk)
    form = UserFormUp(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('profile_user')
    else:
        return render(request, 'new_user.html', {'user': user})


def delete_user(request):
    user = get_object_or_404(User, pk=get_user(request).pk)
    user.delete()
    return redirect('login')


def profile_user(request):
    user = list(User.objects.all().filter(id=get_user(request).pk))
    return render(request, 'profile.html', {'user': user})


def list_user(request):
    pass
