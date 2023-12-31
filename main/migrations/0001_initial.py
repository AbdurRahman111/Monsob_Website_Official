# Generated by Django 3.0 on 2023-12-21 11:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_benner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('benner', models.ImageField(blank=True, help_text='Choose Only .jpg, .jpeg, .png, .webp files PLease..', null=True, upload_to='Home_benner/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])])),
                ('button_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Home Benner',
            },
        ),
        migrations.CreateModel(
            name='home_bottom_benner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=255, null=True)),
                ('title2', models.CharField(blank=True, max_length=255, null=True)),
                ('up_text', models.CharField(blank=True, max_length=255, null=True)),
                ('home_bottom_benner', models.ImageField(blank=True, help_text='Choose Only .jpg, .jpeg, .png, .webp files PLease..', null=True, upload_to='home_bottom_benner/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])])),
                ('button_link', models.URLField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name_plural': 'Home Bottom Benner',
            },
        ),
        migrations.CreateModel(
            name='home_little_benner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='1', max_length=255, null=True)),
                ('benner', models.ImageField(blank=True, help_text='Choose Only .jpg, .jpeg, .png, .webp files PLease..', null=True, upload_to='home_little_benner/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])])),
                ('button_link', models.URLField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name_plural': 'Home Little Benner',
            },
        ),
        migrations.CreateModel(
            name='home_side_benner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('home_side_benner', models.ImageField(blank=True, help_text='Choose Only .jpg, .jpeg, .png, .webp files PLease..', null=True, upload_to='home_bottom_benner/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])])),
                ('button_link', models.URLField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name_plural': 'Home side Benner',
            },
        ),
        migrations.CreateModel(
            name='Shop_now_page_benner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title2', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('Shop_now_page_benner', models.ImageField(blank=True, help_text='Choose Only .jpg, .jpeg, .png, .webp files PLease..', null=True, upload_to='Shop_now_page_benner/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])])),
            ],
            options={
                'verbose_name_plural': 'Shop Now Page Benner',
            },
        ),
    ]
