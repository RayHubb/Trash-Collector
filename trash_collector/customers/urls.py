from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('add_information', views.create, name='add_information'),
    path('account_information/', views.view_account_info, name='account_information'),
    path('change_pickup/', views.change_pickup, name='change_pickup'),
    path('suspend_pickup/', views.suspend_pickup, name='suspend_pickup'),
    path('view_bill/', views.view_bill, name='view_bill'),
]
