from django.urls import include, path
from kanakuputhagam.views import *

urlpatterns = [
    path('', forms, name='allforms'),
]