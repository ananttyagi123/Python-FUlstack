from django.http import HttpRespons
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')