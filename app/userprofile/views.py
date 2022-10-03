from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.views import View

from .forms import CustomAuthenticationForm


class LoginView(View):

    def get(self, request):
        return render(request, 'userprofile/login.html', {'form': AuthenticationForm()})

    def post(self, request):
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )

        if user is None:
            return render(request, 'userprofile/login.html', {'form': AuthenticationForm(), 'error': 'Неправельный логин или пароль'})
        else:
            login(request, user)
            return redirect('home')


class SignupView(View):

    def get(self, request):
        return render(request, 'userprofile/signup.html', {'form': UserCreationForm()})

    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'userprofile/signup.html', {
                    'form': UserCreationForm(), 'error': 'This username already exists!'
                })
        else:
            return render(request, 'userprofile/signup.html', {
                'form': UserCreationForm(), 'error': 'Passwords do not match!'
            })


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('home')


