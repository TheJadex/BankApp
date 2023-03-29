from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User

        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2',
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
        }
