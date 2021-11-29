# Generated by Django 3.2.9 on 2021-11-27 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0001_initial'),
        ('trucks', '0001_initial'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='number_plate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trucks.trucks'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receiver.receiver'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
