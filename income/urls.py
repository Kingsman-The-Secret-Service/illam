from django.urls import path
from income.views import income_details

urlpatterns = [
    path('', income_details.as_view(), name='income')
]