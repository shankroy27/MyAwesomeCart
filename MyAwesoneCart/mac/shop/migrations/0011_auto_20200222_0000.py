# Generated by Django 3.0.2 on 2020-02-21 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200221_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=datetime.date(2020, 2, 22)),
        ),
    ]