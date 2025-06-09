from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomerUser


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control'}))

class EmployeeForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'avatar', 'date_birth', 'address', 'notifications_enabled']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user