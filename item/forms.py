from builtins import int, ValueError, TypeError, super

from django.forms import ModelForm, forms
from .models import Item, Donation


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = '__all__'



class DonationForm(ModelForm):

    class Meta:
        model = Donation
        fields = '__all__'