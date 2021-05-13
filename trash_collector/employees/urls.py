from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.create, name="index"),
    path('daily_run/', views.daily_run, name='daily_run'),
    path('confirm_pickup/', views.confirm_pickup, name='confirm_pickup'),
    path('employee_names/', views.employee_names, name='employee_names'),
    path('employee_zip/', views.employee_zip, name='employee_zip')
]