# Generated by Django 3.0.2 on 2020-02-07 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200128_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=datetime.date(2020, 2, 7)),
        ),
    ]
