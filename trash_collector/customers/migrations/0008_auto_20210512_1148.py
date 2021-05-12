# Generated by Django 3.1.8 on 2021-05-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20210511_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='pickup_date',
        ),
        migrations.AddField(
            model_name='customer',
            name='amount_due',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='customer',
            name='pickup_day',
            field=models.CharField(default='Monday', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='pickup_suspended',
            field=models.BooleanField(default=False),
        ),
    ]