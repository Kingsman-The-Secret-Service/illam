from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from illam.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('kanaku-puthagam/', include('kanakuputhagam.urls')),
    path('', dashboard.dashboard, name="illam.dashboard"),
]
