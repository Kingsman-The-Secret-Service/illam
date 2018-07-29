from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def member(request):
    return render(request, 'member.html')

def source(request):
    return render(request, 'source.html')

def category(request):
    return render(request, 'category.html')