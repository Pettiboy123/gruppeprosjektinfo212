# Generated by Django 4.1.3 on 2022-11-03 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_rename_cid_car_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='id',
            new_name='carId',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='id',
            new_name='customerId',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='id',
            new_name='employeeId',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='orderId',
        ),
    ]