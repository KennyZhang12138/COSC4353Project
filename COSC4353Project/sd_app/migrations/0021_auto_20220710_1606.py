# Generated by Django 3.2.7 on 2022-07-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0020_alter_userprofile_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='location',
        ),
        migrations.AddField(
            model_name='transaction',
            name='delivery_address',
            field=models.CharField(default='DELIVERIES MADE TO ADDRESS IN PROFILE', max_length=35),
        ),
    ]
