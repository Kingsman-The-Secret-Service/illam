from django.contrib import admin
from django.urls import include, path
from .views import category, member, tag, budget, splitup, transaction

urlpatterns = [

    # Category API
    path('category', category.CategoryList.as_view(), name="CategoryList"),
    path('category/<int:pk>/', category.CategoryDetail.as_view(), name="CategoryDetail"),
    
    # Member API
    path('member', member.MemberList.as_view(), name="MemberList"),
    path('member/<int:pk>/', member.MemberDetail.as_view(), name="MemberDetail"),

    # Tag API
    path('tag', tag.TagList.as_view(), name="TagList"),
    path('tag/<int:pk/', tag.TagDetail.as_view(), name="TagDetail"),

    # Budget API
    path('budget', budget.BudgetList.as_view(), name="BudgetList"),
    path('budget/<int:pk>/', budget.BudgetDetail.as_view(), name="BudgetDetail"),

    # Splitup API
    path('splitup', splitup.SplitupList.as_view(), name="SplitupList"),
    path('splitup/<int:pk>/', splitup.SplitupDetail.as_view(), name="SplitupDetail"),

    # Transaction API
    path('transaction', transaction.TransactionList.as_view(), name="TransactionList"),
    path('transaction/<int:pk>/', transaction.TransactionDetail.as_view(), name="TransactionDetail"),
]

