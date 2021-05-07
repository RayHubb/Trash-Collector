from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    pick_up_date = models.CharField(max_length=50, default='day')
    one_time_pick_up = models.DateField(auto_now=True)
    account_balance = models.IntegerField(default=0)
    pick_up_address = models.CharField(max_length=50, default='address')
    pick_up_city = models.CharField(max_length=50, default='city')
    pick_up_state = models.CharField(max_length=50, default='state')
    pick_up_zip = models.CharField(max_length=50, default=48217)
