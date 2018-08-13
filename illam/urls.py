from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('', include('kanakuputhagam.urls')),
]
