from django.urls import include, path
from kanakuputhagam.views import dashboard, budget, splitup, transaction, category, member, tag


urlpatterns = [

    # Dashboard
    path('',dashboard.dashboard, name='kp.dashboard'),

    # Budget
    path('budget/', budget.BudgetList.as_view(), name='budget-list'),
    path('budget/add/', budget.BudgetCreate.as_view(), name='budget-add'),
    path('budget/<int:pk>/', budget.BudgetUpdate.as_view(), name='budget-update'),
    path('budget/<int:pk>/delete/', budget.BudgetDelete.as_view(), name='budget-delete'),

    # SplitUp
    path('splitup/', splitup.SplitupList.as_view(), name='splitup-list'),
    path('splitup/add/', splitup.SplitupCreate.as_view(), name='splitup-add'),
    path('splitup/add/<str:type>', splitup.SplitupCreate.as_view(), name='splitup-add'),
    path('splitup/<int:pk>/', splitup.SplitupUpdate.as_view(), name='splitup-update'),
    path('splitup/<int:pk>/delete/', splitup.SplitupDelete.as_view(), name='splitup-delete'),

    # Transaction
    path('transaction/', transaction.TransactionList.as_view(), name='transaction-list'),
    path('transaction/add/', transaction.TransactionCreate.as_view(), name='transaction-add'),
    path('transaction/add/<str:type>', transaction.TransactionCreate.as_view(), name='transaction-add'),
    path('transaction/<int:pk>/', transaction.TransactionUpdate.as_view(), name='transaction-update'),
    path('transaction/<int:pk>/delete/', transaction.TransactionDelete.as_view(), name='transaction-delete'),

    # Category
    path('category/', category.CategoryList.as_view(), name='category-list'),
    path('category/add/', category.CategoryCreate.as_view(), name='category-add'),
    path('category/<int:pk>/', category.CategoryUpdate.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', category.CategoryDelete.as_view(), name='category-delete'),

    # Member
    path('member/', member.MemberList.as_view(), name='member-list'),
    path('member/add/', member.MemberCreate.as_view(), name='member-add'),
    path('member/<int:pk>/', member.MemberUpdate.as_view(), name='member-update'),
    path('member/<int:pk>/delete/', member.MemberDelete.as_view(), name='member-delete'),

    # Tag
    path('tag/', tag.TagList.as_view(), name='tag-list'),
    path('tag/add/', tag.TagCreate.as_view(), name='tag-add'),
    path('tag/<int:pk>/', tag.TagUpdate.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', tag.TagDelete.as_view(), name='tag-delete'),

]