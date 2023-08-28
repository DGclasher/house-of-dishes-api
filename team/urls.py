from .views import *
from django.urls import path

urlpatterns = [
    path('cofounders/', CoFounderListView.as_view(), name='cofounders'),
    path('employee/all/', EmployeeListAllView.as_view(), name='employee_all'),
    path('employee/<str:employee_id>/', EmployeeListView.as_view(), name='employee'),
]