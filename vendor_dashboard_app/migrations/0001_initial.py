# Generated by Django 3.0 on 2023-12-21 11:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendor_registration_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=40)),
                ('vendor_shop_name', models.CharField(max_length=100)),
                ('vendor_shop_url', models.TextField(blank=True, null=True)),
                ('vendor_address', models.CharField(blank=True, max_length=200, null=True)),
                ('vendor_shop_logo', models.TextField(blank=True, null=True)),
                ('vendor_shop_banner', models.TextField(blank=True, null=True)),
                ('vendor_phone_no', models.CharField(max_length=100)),
                ('vendor_email', models.EmailField(max_length=100)),
                ('vendor_password', models.CharField(max_length=100)),
                ('vendor_activation', models.BooleanField(default=False)),
                ('join_date', models.DateField(blank=True, default=datetime.datetime(2023, 12, 21, 17, 9, 25, 791073))),
                ('featured_vendor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='vendor_PO_NUMBER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor_po_Number', models.IntegerField()),
                ('Vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_dashboard_app.vendor_registration_table')),
            ],
        ),
        migrations.CreateModel(
            name='vendor_payment_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_payment_roll', models.CharField(choices=[('SSLCommerz', 'SSLCommerz'), ('Bank Deposite', 'Bank Deposite')], default='SSLCommerz', max_length=20)),
                ('Bank_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Account_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Account_Number', models.IntegerField(blank=True, null=True)),
                ('Branch', models.CharField(blank=True, max_length=200, null=True)),
                ('Routing_Number', models.IntegerField(blank=True, null=True)),
                ('SSL_operator', models.CharField(blank=True, choices=[('Bkash', 'Bkash'), ('Nogod', 'Nogod')], max_length=20, null=True)),
                ('SSL_Mobile_Number', models.IntegerField(blank=True, null=True)),
                ('Vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_dashboard_app.vendor_registration_table')),
            ],
        ),
    ]
