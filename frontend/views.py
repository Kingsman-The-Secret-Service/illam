from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def budget(request):
    return render(request, 'budget.html')

@login_required
def income(request):
    return render(request, 'income.html')

@login_required
def expense(request):
    return render(request, 'expense.html')

@login_required
def member(request):
    return render(request, 'member.html')

@login_required
def source(request):
    return render(request, 'source.html')

@login_required
def category(request):
    return render(request, 'category.html')