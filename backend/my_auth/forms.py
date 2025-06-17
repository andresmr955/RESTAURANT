from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomerUser

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={"class": 'form-control'}))

