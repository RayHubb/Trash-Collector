from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps


# index view of customers who are in the zip code,have non suspended accounts, pickup is
# today or the one time pick up is today.


def create(request):
    if request.method == 'POST':
        employee_names = request.POST.get('employee_name')
        employee_zip = request.POST.get(name="name", employee_zip="employee_zip")
    pass


def daily_run(request, daily_run):
    if request.method == 'POST':
        user = request.user
        daily_run = daily_run.objects.get(daily_run="")
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


def confirm_pickup(request, confirm_pickup):
    if request.method == 'POST':
        user = request.user
        confirm_pickup: confirm_pickup.objects.get(confirm_pickup="")
        context = {

        }
        return render(request, 'employees/confirm_pickup.html', context)
        pass


def employee_names(request, employee):
    if request.method == 'POST':
        user = request.user
        employee = employee.objects.get(name="")
        context = {
            employee: employee
        }
        return render(request, 'employees/names.html', context)
        pass


def employee_zip(request, employee):
    if request.method == 'POST':
        user = request.user
        employee = employee.objects.get(employee_zip="")
        context = {
            employee: employee
        }
        return render(request, 'employees/zip.html', context)
        pass

