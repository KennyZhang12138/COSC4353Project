# Generated by Django 4.0.5 on 2022-06-30 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0003_remove_transaction_customer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sd_app.userprofile'),
            preserve_default=False,
        ),
    ]