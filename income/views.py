from django.shortcuts import render
from django.views.generic.base import TemplateView 

# Create your views here.
class income_details(TemplateView):
    template_name = "income.html"