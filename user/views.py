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
    user = get_object_or_404(User, pk=get_user(request).pk)
    form = UserForm(request.POST or None, instance=user)

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
    main_user = User.objects.filter(pk=get_user(request).pk)
    values_user = list(main_user.values('username', 'first_name', 'last_name', 'email'))
    user = values_user[0].get("username", None)
    first_name = values_user[0].get("first_name", None)
    last_name = values_user[0].get("last_name", None)
    email = values_user[0].get("email", None)
    return render(request, 'profile_user.html',
                  {'user': user, 'first_name': first_name, 'last_name': last_name, 'email': email})


def list_user(request):
    pass
