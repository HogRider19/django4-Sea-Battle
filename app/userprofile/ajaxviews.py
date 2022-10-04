from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View


def check_username_for_uniqueness(request):
    """Проверка допустимости имении пользователя"""
    user = User.objects.filter(username=request.GET.get('username', None).replace(' ', ''))

    is_admissible = False if user else True

    return JsonResponse({'is_admissible': is_admissible})
