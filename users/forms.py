from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from .models import RegularUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class RegistrationForm(UserCreationForm):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
