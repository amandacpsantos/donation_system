from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from django.contrib.auth import get_user_model, get_user
from .models import Item, Donation



@login_required()
def dashboard(request):
     return render(request, 'dashboard.html')


@login_required()
def list_item(request):
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
    return render(request, "list_item.html", {'donations': donations})
