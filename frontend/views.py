from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def budget(request):
    return render(request, 'budget.html')

@login_required
def splitup(request):
    return render(request, 'splitup.html')

@login_required
def transaction(request):
    return render(request, 'transaction.html')

@login_required
def category(request):
    return render(request, 'category.html')

@login_required
def member(request):
    return render(request, 'member.html')

@login_required
def tag(request):
    return render(request, 'tag.html')