from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.

    print(user)
    return render(request, 'customers/index.html')


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        pickup_day = request.POST.get('pickup_day')
        pickup_address = request.POST.get('pickup_address')
        pickup_city = request.POST.get('pickup_city')
        pickup_state = request.POST.get('pickup_state')
        pickup_zip = request.POST.get('pickup_zip')
        new_customer = Customer(user=user, name=name, pickup_day=pickup_day, pickup_address=pickup_address,
                                pickup_city=pickup_city, pickup_state=pickup_state, pickup_zip=pickup_zip)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:account_information'))
    else:
        return render(request, 'customers/add_information.html')


def view_account_info(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    context = {
        "customer": customer
    }
    return render(request, 'customers/account_information.html', context)


def change_pickup(request):
    if request.method == 'POST':
        user = request.user
        old_day = Customer.pickup_day.get(user=user)
    return render(request, 'customers/change_pickup.html')
    pass

def suspend_pickup(request):
    context = {

    }
    return render(request, 'customers/suspend_pickup.html', context)


def view_bill(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    total_amount_due = customer.amount_due
    context = {
        "total_amount_due": total_amount_due
    }
    return render(request, 'customers/view_bill.html', context)

# if request.method == 'POST':
# user = request.user
# name = request.POST.get('name')
# pickup_day = request.POST.get('pickup_day')
# pickup_address = request.POST.get('pickup_address')
# pickup_city = request.POST.get('pickup_city')
# pickup_state = request.POST.get('pickup_state')
# pickup_zip = request.POST.get('pickup_zip')
# user = Customer(user=user, name=name, pickup_day=pickup_day, pickup_address=pickup_address, pickup_city=pickup_city,
#                 pickup_state=pickup_state, pickup_zip=pickup_zip)
# user.save()
