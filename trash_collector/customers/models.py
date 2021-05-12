from django.db import models
from django.contrib.auth.models import Group


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    pickup_address = models.CharField(max_length=50, default='address')
    pickup_city = models.CharField(max_length=50, default='city')
    pickup_state = models.CharField(max_length=50, default='state')
    pickup_zip = models.CharField(max_length=50, default=48217)
    pickup_day = models.CharField(max_length=20, default='Monday')
    pickup_suspended = models.BooleanField(default=False)
    amount_due = models.IntegerField(default=0.00)

    def __str__(self):
        return self.name
