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

from django.contrib.auth import views as auth_views
from KanakuPuthagam.views import member, category


urlpatterns = [
    
    # Admin
    path('admin/', admin.site.urls),

    ############################## API ##################################

    # Member API
    path('members', member.MemberList.as_view()),
    path('members/<int:pk>/', member.MemberDetail.as_view()),

    # Category API
    path('category', category.CategoryList.as_view()),
    
    ############################### UI/UX ###############################

    # Authentication
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),

    # Dashboard
    # path('', ),
]

