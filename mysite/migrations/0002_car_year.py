# Generated by Django 4.1.2 on 2022-10-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="year",
            field=models.CharField(default=2000, max_length=50),
            preserve_default=False,
        ),
    ]
