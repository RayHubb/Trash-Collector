from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


# Get the Customer model from the other app, it can now be used to query the db
def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'employees/index.html')


# index view of customers who are in the zip code,have non suspended accounts, pickup is
# today or the one time pick up is today.

def daily_run(request):
    user = request.user
    context = {

    }
    return render(request, 'employees/daily_run.html', context)
    # todays_pick_ups = Customers.Object.get('pick_up_date')
    # customer_zip_code = Customers.Object.get('
    # pass
    # filter customers in the area by a particular day

    # confirmed pickups have a charge applied

    # Navbar to direct employee to links for default daily view and any other pages needed related
    # to the daily filter.


def confirm_pickup(request):
    user = request.user
    context = {

    }
    return render(request, 'employees/confirm_pickup.html', context)
