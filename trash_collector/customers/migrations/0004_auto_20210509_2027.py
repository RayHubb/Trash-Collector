# Generated by Django 3.1.8 on 2021-05-10 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_pick_up_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='temp_suspend_end',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='temp_suspend_start',
            field=models.DateField(auto_now=True),
        ),
    ]
