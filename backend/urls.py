from django.contrib import admin
from django.urls import include, path
from .views import member, category, source, income, tag, expenses, budget

urlpatterns = [
    
    # Member API
    path('members', member.MemberList.as_view(), name="memberList"),
    path('member/<int:pk>/', member.MemberDetail.as_view()),

    # Source API
    path('sources', source.SourceList.as_view(), name="sourceList"),
    path('source/<int:pk>', source.SourceDetail.as_view()),

    # Category API
    path('categories', category.CategoryList.as_view(), name="categoriesList"),

    # Income API
    path('incomes', income.IncomeList.as_view(), name="incomeList"),
    path('income/<int:pk>/', income.IncomeDetail.as_view()),

    # Expenses API
    path('expenses', expenses.ExpensesList.as_view(), name="expensesList"),
    path('expenses/<int:pk>/', expenses.ExpensesDetail.as_view()),

    # Budget API
    path('budget', expenses.ExpensesList.as_view(), name="budgetList"),
    path('budget/<int:pk>/', expenses.ExpensesDetail.as_view()),

    #Tag API
    path('tag', tag.TagList.as_view(), name="tagList"),
    path('tag/<int:pk/', tag.TagDetail.as_view())
]

