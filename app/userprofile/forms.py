from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для отправки комментариев к фильму"""
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'name': "username",
                'type': "username",
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'name': "password",
                'type': "password",
            }),
        }