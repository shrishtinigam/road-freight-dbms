# Generated by Django 3.2.9 on 2021-11-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck_Owner',
            fields=[
                ('truck_owner_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('truck_owner_name', models.CharField(max_length=45)),
                ('num_trucks', models.CharField(max_length=45)),
            ],
        ),
    ]
