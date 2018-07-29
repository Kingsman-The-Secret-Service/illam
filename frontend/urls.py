from django.urls import include, path
from frontend import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.dashboard),
    path('member', views.member),
    path('source', views.source),
    path('category', views.category),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
]