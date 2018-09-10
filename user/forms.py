from django.forms import ModelForm
from .models import Person
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ['username', 'email']


class UserFormUp(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone']
