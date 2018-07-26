from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.

def expense_home(request):
    return HttpResponse("Welcome to Magic Expense page")
