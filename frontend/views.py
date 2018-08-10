from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def budget(request):
    return render(request, 'budget.html')

def budgetForm(request):
    from frontend.forms import BudgetForm
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = BudgetForm()
    return render(request, 'budget/form.html', {'form': form})

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