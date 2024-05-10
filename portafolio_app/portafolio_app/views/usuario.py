from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def load(request):
    return render(request, 'usuario.html')