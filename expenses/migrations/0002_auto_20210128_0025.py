# Generated by Django 3.0.1 on 2021-01-27 23:25

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="date",
            field=models.DateField(default=datetime.date(2021, 1, 28)),
        ),
    ]
