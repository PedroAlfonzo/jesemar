from django.urls import path
from . import views

urlpatterns = [
    path('', views.webjesemar_list, name='webjesemar_list'),
]