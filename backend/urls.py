from django.contrib import admin
from django.urls import include, path
from .views import member, category, source, income

urlpatterns = [
    
    # Member API
    path('members', member.MemberList.as_view()),
    path('member/<int:pk>/', member.MemberDetail.as_view()),

    # Source API
    path('sources', source.SourceList.as_view()),
    path('source/<int:pk>', source.SourceDetail.as_view()),

    # Category API
    path('categories', category.CategoryList.as_view()),

    # Income API
    path('incomes', income.IncomeList.as_view()),
    path('income/<int:pk>/', income.IncomeDetail.as_view()),
]

