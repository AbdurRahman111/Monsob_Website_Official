# Generated by Django 3.0 on 2023-12-24 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20231223_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_table',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 24, 10, 50, 32, 648105)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Order_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 24, 10, 50, 32, 648105)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 24, 10, 50, 32, 648105)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 24, 10, 50, 32, 648105)),
        ),
        migrations.AlterField(
            model_name='order_table_2',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 24, 10, 50, 32, 649101)),
        ),
        migrations.AlterField(
            model_name='order_table_3_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 24, 10, 50, 32, 651096)),
        ),
        migrations.AlterField(
            model_name='order_table_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 24, 10, 50, 32, 651096)),
        ),
    ]
