from django.shortcuts import render
from kanakuputhagam.forms import *

def forms(request):
    bform = BudgetForm()
    return render(request, 'budget/form.html', {'bform': bform})
