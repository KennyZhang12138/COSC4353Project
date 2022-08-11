# Generated by Django 3.2.7 on 2022-07-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0024_alter_transaction_suggested_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='suggested_price',
            field=models.DecimalField(decimal_places=2, default='4.56', max_digits=6),
        ),
    ]