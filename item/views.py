from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required

from donation.settings import EMAIL_HOST_USER
from .forms import ItemForm, MessageForm
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.models import User
from .models import Item, Donation
from user.models import Person
from django.core.mail import send_mail
from .enum_collection import STATUS_CHOICES
from django.db.models import Q


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
        return render(request, 'new_item.html', {'form': form})


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


@login_required()
def cancel_donation(request, id_item):
    Item.objects.filter(pk=id_item).update(status=STATUS_CHOICES[0][0])
    Donation.objects.filter(item_id=id_item).delete()
    return HttpResponseRedirect('/dashboard/list_item/')


@login_required()
def make_donation(request, id_item):
    # Mudar status do item
    Item.objects.filter(pk=id_item).update(status=STATUS_CHOICES[1][0])
    item = Item.objects.get(pk=id_item)

    # Criar doação e salvar
    donation = Donation(item=item)
    donation.save()

    return redirect('list_item')


@login_required()
def list_donation(request):
    donations = Donation.objects.filter(item__status=STATUS_CHOICES[1][0])
    return render(request, "list_donation.html", {'donations': donations})


@login_required()
def historic_donation(request):
    donations = Donation.objects.filter((Q(taker_id=get_user(request).pk) | Q(item__donor_id=get_user(request).pk)) and
                                        (Q(item__status='RESERVED') | Q(item__status='DONATED')))
    return render(request, "historic_donation.html", {'donations': donations})


@login_required()
def check_donation(request, id_item):
    Item.objects.filter(pk=id_item).update(status=STATUS_CHOICES[3][0])
    return HttpResponseRedirect('/dashboard/historic_donation/')


@login_required()
def cancel_reservation_donation(request, id_item, id_donation):
    Item.objects.filter(pk=id_item).update(status=STATUS_CHOICES[1][0])
    Donation.objects.filter(pk=id_donation).update(taker_id=None)

    return HttpResponseRedirect('/dashboard/historic_donation/')

@login_required()
def send_message(request, id_item, id_donation):

    # DADOS DO ITEM
    query_item = Item.objects.filter(pk=id_item)
    values_item = list(query_item.values())

    id_donor = values_item[0].get("donor_id", None)
    name_item = values_item[0].get("name", None)
    print(name_item)

    # DADOS DO INTERESSADO
    main_user = User.objects.filter(pk=get_user(request).pk)
    values_user = list(main_user.values())
    print(values_user)
    name_user = values_user[0].get("username", None)
    email_user = values_user[0].get("email", None)
    print(name_user)
    print(email_user)

    # DADOS DO DONO DO ITEM
    query_donor = User.objects.filter(pk=id_donor)
    values_donor = list(query_donor.values())
    email_donor = values_donor[0].get("email", None)
    name_donor = values_donor[0].get("username", None)
    print(name_donor)
    print(email_donor)

    # DADOS PARA O EMAIL
    from_email = EMAIL_HOST_USER
    to_email = email_donor
    subject_email = "Alguém tem interesse na doação!"
    body_email = "Olá {}, alguém está interessado no item '{}'. Vocês podem trocar e-mails e combinar como será a doação.\n" \
                 "Dados para contados:\n" \
                 "Nome: {}\n" \
                 "Email: {}\n\n" \
                 "Caso a doação for concluída, não esqueça em finalizá-la." \
                 "".format(name_donor, name_item, name_user, email_user)

    success = send_mail(
        subject_email,
        body_email,
        from_email,
        [to_email],
        fail_silently=False)

    if success == 1:
        query_item.update(status=STATUS_CHOICES[2][0])
        Donation.objects.filter(pk=id_donation).update(taker_id=get_user(request).pk)
        return HttpResponseRedirect('/dashboard/historic_donation/')

    return HttpResponseRedirect('/dashboard/')

