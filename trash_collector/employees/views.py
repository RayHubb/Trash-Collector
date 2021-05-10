from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')

    # index view of customers who are in the zip code,have non suspended accounts, pickup is
    # today or the one time pick up is today.

def daily_pick_ups(request):
    pass
    #   todays_pick_ups = Customers.Object.get('pick_up_date')
    #  customer_zip_code = Customers.Object.get('
    # pass
    # filter customers in the area by a particular day

    # confirmed pickups have a charge applied

    # Navbar to direct employee to links for default daily view and any other pages needed related
    # to the daily filter.

