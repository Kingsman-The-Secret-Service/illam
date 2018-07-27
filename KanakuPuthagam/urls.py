"""KanakuPuthagam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from graphene_django.views import GraphQLView
from django.contrib.auth import views as auth_views
from KanakuPuthagam import views


urlpatterns = [
    
    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),

    # Member API
    path('members', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view()),

    # Source API
    path('source', views.SourceList.as_view()),
    path('source/<int:pk>', views.SourceDelail.as_view()),

    # Income API
    path('income', views.IncomeList.as_view()),
    path('income/<int:pk>/', views.IncomeDetail.as_view()),
    # Category API
    

]

