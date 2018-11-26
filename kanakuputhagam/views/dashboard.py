from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from kanakuputhagam.models import Category, Budget, Splitup, Transaction

@login_required
def dashboard(request):

    data = {}
    budgets = Budget.objects.filter(user = request.user)
    data['budgets'] = budgets
    budget = budgets.first()
    categories = Category.objects.filter(user = request.user)

    if budget and categories:
    
        splitups = Splitup.objects.filter(user = request.user, budget=budget)
        transactions = Transaction.objects.filter(user = request.user, date__gte = budget.start_date, date__lte = budget.end_date)
        
        incomeData = [['Category', 'Planned', 'Actual']]
        savingData = [['Category', 'Planned', 'Actual']]
        expenseData = [['Category', 'Planned', 'Actual']]

        for category in categories:

            splitupAmount = 0
            for splitup in splitups.filter(category = category.id):
                splitupAmount += splitup.amount
            
            transactionAmount = 0
            for transaction in transactions.filter(category = category.id):
                transactionAmount += transaction.amount

            if category.type == 'INCOME':
                incomeData.append([category.name, splitupAmount, transactionAmount])
                
            if category.type == 'SAVING':
                savingData.append([category.name, splitupAmount, transactionAmount])

            if category.type == 'EXPENSE':
                expenseData.append([category.name, splitupAmount, transactionAmount])

            data['incomeData'] = incomeData
            data['savingData'] = savingData
            data['expenseData'] = expenseData
        
    return render(request, 'kp/dashboard.html', data)
