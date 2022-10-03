from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomAuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


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
    