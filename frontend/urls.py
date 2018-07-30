from django.urls import include, path
from frontend import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('budget/', views.budget, name='budget'),
    path('income/', views.income, name='income'),
    path('expense/', views.expense, name='expense'),
    path('member/', views.member, name='member'),
    path('source/', views.source, name='source'),
    path('category/', views.category, name='category'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

]