# Generated by Django 4.1.2 on 2022-10-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0003_car_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="status",
            field=models.CharField(default="Available", max_length=50),
            preserve_default=False,
        ),
    ]
