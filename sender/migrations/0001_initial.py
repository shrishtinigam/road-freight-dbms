# Generated by Django 3.2.9 on 2021-11-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('sender_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=45)),
                ('driver_id', models.CharField(max_length=45)),
            ],
        ),
    ]