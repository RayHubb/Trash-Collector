# Generated by Django 3.1.8 on 2021-05-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210507_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pick_up_zip',
            field=models.CharField(default=48217, max_length=50),
        ),
    ]
