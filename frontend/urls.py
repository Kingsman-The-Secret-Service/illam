from django.urls import include, path
from frontend import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('budget/', views.budget, name='budget'),
    path('splitup/', views.splitup, name='splitup'),
    path('transaction/', views.transaction, name='transaction'),
    path('category/', views.category, name='category'),
    path('member/', views.member, name='member'),
    path('tag/', views.tag, name='tag'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

]