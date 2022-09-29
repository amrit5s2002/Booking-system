from django.urls import path
from .views import *

print("booking url")
urlpatterns = [
    path('',welcome,name = 'welcome')
]
