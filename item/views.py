from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required

from donation.settings import EMAIL_HOST_USER
from .forms import ItemForm, MessageForm
from django.contrib.auth import get_user_model, get_user
from .models import Item, Donation
from django.core.mail import send_mail




@login_required()
def dashboard(request):
     return render(request, 'dashboard.html')


@login_required()
def list_item(request):
    print(get_user(request))
    itens = Item.objects.all().filter(donor_id=get_user(request).pk)
    return render(request, "list_item.html", {'itens': itens})


@login_required
def new_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.donor = get_user(request)
        item.save()
        return redirect('dashboard')
    else:
        return render(request, 'new_item.html', {'form':form})


@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('list_item')


@login_required
def update_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('list_item')
    else:
        return render(request, 'new_item.html', {'form': form})


def load_category(request):
    category_id = request.GET.get('category')
    categories = Category.objects.filter(category_id=category_id).order_by('type')
    return render(request, 'list_item.html', {'categories': categories})


@login_required()
def make_donation(request, id_item):
    Item.objects.filter(pk=id_item).update(status='EM_DOACAO')
    item = Item.objects.get(pk=id_item)

    donation = Donation(item=item)
    donation.save()

    return redirect('list_item')


@login_required()
def list_donation(request):
    donations = Donation.objects.all()
    print(donations)
    return render(request, "list_donation.html", {'donations': donations})


@login_required()
def send_message(request, id_item):
    item = Item.objects.get(pk=id_item)

    print(item.donor)

    send_mail(
        'TESTE LAB',
        'TESTE',
        EMAIL_HOST_USER,
        ['contatoacps@gmail.com'],
        fail_silently=False,
    )
    return HttpResponseRedirect('/dashboard/')


def open_message(request):
    return render(request, 'send_message.html')

@login_required
def new_message(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        message_fields = form.save(commit=False)

        send_mail(
            message_fields.subject,
            message_fields.body,
            EMAIL_HOST_USER,
            [message_fields.to_email],
            fail_silently=False,
        )

        return HttpResponseRedirect('/dashboard/')

    else:
        return render(request, 'send_message.html', {'form':form})
