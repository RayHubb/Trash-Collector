from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps


# index view of customers who are in the zip code,have non suspended accounts, pickup is
# today or the one time pick up is today.


def create(request):
    if request.method == 'POST':
        customer_within_zipcode = request.POST.get('customers_within_zipcode')
        employee_names = request.POST.get('employee_name')
        describe_employee = Employee(name=name, customer_zipcode=customer_zipcode)
    pass


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
    pass


def confirm_pickup(request):
    user = request.user
    context = {

    }
    return render(request, 'employees/confirm_pickup.html', context)
    pass


def employee_names(request):
    user = request.user
    employee = employee.objects.get(name="")
    context = {
        "employee": employee
    }
    pass


def customer_within_zipcode(request):
    user = request.user
    customer = customer.objects.get(pickup_zip="")
    context = {
        "costumer": customer
    }
    return render(request, 'employees/customers_within_zipcode')
    pass

