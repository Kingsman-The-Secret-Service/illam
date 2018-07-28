from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views
from KanakuPuthagam.views import member, category, source, income


urlpatterns = [
    
    # Admin
    path('admin/', admin.site.urls),

    ############################## API ##################################

    # Member API
    path('members', member.MemberList.as_view()),
    path('members/<int:pk>/', member.MemberDetail.as_view()),

    # Source API
    path('source', source.SourceList.as_view()),
    path('source/<int:pk>', source.SourceDetail.as_view()),

    # Category API
    path('category', category.CategoryList.as_view()),

    # Income API
    path('income', income.IncomeList.as_view()),
    path('income/<int:pk>/', income.IncomeDetail.as_view()),
    
    ############################### UI/UX ###############################

    # Authentication
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),

    # Dashboard
    # path('', ),
]

