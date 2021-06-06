from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from shop.models import ShippingAddress

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "name",
        "type": "text",
        "placeholder": "Email",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'Email'"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "name",
        "type": "text",
        "placeholder": "Username",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'Username'"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "name",
        "type": "text",
        "placeholder": "Password",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'Password'"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "name",
        "type": "text",
        "placeholder": "Retype Password",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'Retype Password'"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


       