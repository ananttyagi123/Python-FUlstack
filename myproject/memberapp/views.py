from django.shortcuts import render
from django.http import HttpResponse


def members(request):
    return HttpResponse("This is the members page of my Django project.")