from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kp/', include('kanakuputhagam.urls')),
    # path('api/', include('backend.urls')),
    path('', include('frontend.urls')),
]
