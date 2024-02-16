# Generated by Django 3.0.1 on 2021-04-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0017_auto_20210415_1803"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.CharField(
                choices=[
                    ("Atm withdrawl", "Atm withdrawl"),
                    ("Bar tabs", "Bar tabs"),
                    ("Monthly bill", "Monthly bill"),
                    ("Online shopping", "Online shopping"),
                    ("Electronics", "Electronics"),
                    ("Groceries", "Groceries"),
                    ("Taxi fare", "Taxi fare"),
                    ("Miscellaneous", "Miscellaneous"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
