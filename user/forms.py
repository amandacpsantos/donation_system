from django.forms import ModelForm
from .models import Person
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ['username', 'email']