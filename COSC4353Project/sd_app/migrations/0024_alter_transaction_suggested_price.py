# Generated by Django 3.2.7 on 2022-07-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0023_alter_transaction_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='suggested_price',
            field=models.CharField(default='$4.56', max_length=5),
        ),
    ]