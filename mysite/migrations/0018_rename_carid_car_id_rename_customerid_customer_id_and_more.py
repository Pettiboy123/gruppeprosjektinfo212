# Generated by Django 4.1.3 on 2022-11-03 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_rename_id_car_carid_rename_id_customer_customerid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='carId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employeeId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderId',
            new_name='id',
        ),
    ]